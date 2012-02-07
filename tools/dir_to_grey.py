#!/usr/bin/env python3
from argparse import ArgumentParser
import subprocess
import os



def main():
    args_parser = ArgumentParser(description="Converts a directory of images to"
                                             "grayscale")
    args_parser.add_argument('img_dir')
    args = args_parser.parse_args()    
    img_dir = args.img_dir
    for img_name in os.listdir(img_dir): 
        subprocess.check_call(['mogrify', '-resize', '128x128', '-normalize', '-colorspace', 'Gray', os.path.join(img_dir, img_name)])

if __name__ == '__main__':
    exit(main())
