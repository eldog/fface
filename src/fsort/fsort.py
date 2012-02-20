#!/usr/bin/env python2.7
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from argparse import ArgumentParser
import multiprocessing
import os
import pickle
import sys
import Tkinter as tk

from matplotlib import pyplot
from PIL import Image, ImageTk

class FsortGui(object):
    def __init__(self, compare_queue):
        super(FsortGui, self).__init__()
        self.compare_queue = compare_queue
        self.enabled = False
        self.compare_count = 0

        self.tk = tk.Tk()
        self.id = None
        self.tk.protocol("WM_DELETE_WINDOW", self._close)
        for i in range(2):
            self.tk.columnconfigure(i, weight=1)
        self.tk.rowconfigure(0, weight=1)
        self.tk.rowconfigure(1, weight=1)
        self.tk.title('Fsort')
        
        self.tk.bind('<Left>', lambda e: self._on_compare(1))
        self.tk.bind('<Right>', lambda e: self._on_compare(-1))
        def make_button(i, result):
            b = tk.Button(master=self.tk, command=lambda:
                    self._on_compare(result))
            b.grid(row=0, column=i, padx=5, pady=5, stick=tk.NSEW)
            return b
        
        self.b_left = make_button(0, 1)
        self.b_right = make_button(1,  -1)
       
        self.count_label = tk.Label(master=self.tk, 
                                    text=self._get_compare_count())
        self.count_label.grid(row=1, column=0, padx=5, pady=5, stick=tk.NSEW)
    
        self._poll_queue()
        
    def mainloop(self):
        self.tk.mainloop()

    def _close(self):
        self.enabled = False
        if self.id is not None:
            self.tk.after_cancel(self.id)
        self.compare_queue.send(None)
        self.tk.destroy()

    def _load_image(self, button, image_path):
        button.image = Image.open(image_path)
        button.photo = ImageTk.PhotoImage(button.image)
        button.config(image=button.photo)

    def _get_compare_count(self):
        return 'comparisons so far: %d' % self.compare_count

    def _on_compare(self, result):
        if self.enabled:
            self.enabled = False
            self.compare_count += 1
            self.count_label.config(text=self._get_compare_count())
            self.compare_queue.send(result)
            self._poll_queue()

    def _poll_queue(self):
        if self.compare_queue.poll():
            self.id = None
            msg = self.compare_queue.recv()
            if msg is None:
                self._close()
            else:
                f1, f2 = msg
                self._load_image(self.b_left, f1)
                self._load_image(self.b_right, f2)
                self.enabled = True
        else:
            self.id = self.tk.after(100, self._poll_queue)

def fsort(compare_queue, image_dir, cache_path, out_path):
    if os.path.isfile(cache_path):
        with open(cache_path, 'rb') as cache_file:
            cache = pickle.load(cache_file)
    else:
        cache = {}
    faces = set()
    for item in os.listdir(image_dir):
        name, ext = os.path.splitext(item)
        if ext == '.jpg':
            faces.add(os.path.join(image_dir, item))

   
    def cmp(f1, f2):
        c = (os.path.basename(f1), os.path.basename(f2))
        if c in cache:
            return cache[c]
        compare_queue.send((f1, f2))
        result = compare_queue.recv()
        if result is None:
            raise KeyboardInterrupt
        cache[c] = result
        return result
    
    try:
        sorted_faces = sorted(faces, cmp=cmp)
    except KeyboardInterrupt:
        return
    finally:
        print('writing cache')
        with open(cache_path, 'wb') as cache_file:
            pickle.dump(cache, cache_file)

    compare_queue.send(None)
    with open(out_path, 'w') as out_file:
        out_file.write('\n'.join(map(os.path.basename, sorted_faces)))

def plot_faces(image_dir, face_file_path, rank_image_out_file):
    with open(face_file_path, 'r') as face_file:
        faces = face_file.read().split('\n')
    scores = range(len(faces)) 
    fig = pyplot.figure(figsize=(20,4))
    fig.xlabel('ranking')
    fig.title('sorted face rankings', fontsize='small')
    for i, image in enumerate(faces):
        axes.imshow(Image.open(os.path.join(image_dir, image)),
            extent=(scores[i] + 0.2, scores[i] - 0.2, 0.2,- 0.2))
    with open(rank_image_out_file, 'wb') as rank_image_file:
        fig.savefig(rank_image_file, dpi=96, format='png')
    fig.show()

def build_argument_parser():
    argument_parser = ArgumentParser()
    argument_parser.add_argument('face_directory', 
                                 help='the directory containing face images')
    argument_parser.add_argument('cache_file',
                                 help='the cache of the sort so we can take a'
                                      ' breather')
    argument_parser.add_argument('out_file',
                                 help='the output file where the ordered faces'
                                      ' will be written to')
    argument_parser.add_argument('rank_image_out_file',
                                 help='the output file where the image of the'
                                      ' ranked faces will be written to')
    argument_parser.add_argument('--no-sort', action='store_true')
    return argument_parser

def main(argv=None):
    if argv is None:
        argv = sys.argv
    argument_parser = build_argument_parser()
    args = argument_parser.parse_args(argv[1:])
    if not args.no_sort:
        gui_conn, fsort_conn = multiprocessing.Pipe()
        fsort_process = multiprocessing.Process(target=fsort, 
                                                args=(fsort_conn,
                                                      args.face_directory,
                                                      args.cache_file,
                                                      args.out_file))
        fsort_process.start()
        fsort_gui = FsortGui(gui_conn)
        fsort_gui.mainloop()
        fsort_process.join()
    plot_faces(args.face_directory, args.out_file, args.rank_image_out_file)
    return 0

if __name__ == '__main__':
    exit(main())

