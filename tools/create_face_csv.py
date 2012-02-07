#!/bin/bash

import csv
import os

with open('face_scores.csv', 'wb') as f:
    csv_writer = csv.writer(f)
    scores = []
    for i in os.listdir('data/faces'):
        score = int(''.join(i.split('-')[1].split('.')[:2]))
        scores.append(score)
    score_set = set(scores)
    for score in score_set:
        csv_writer.writerow([score, scores.count(score)])

