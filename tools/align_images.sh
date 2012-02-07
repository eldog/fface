#!/bin/bash

./face_align_lister.py ../data/eccv2010_beauty_data/eccv2010_split1.csv ../data/eccv2010_beauty_data/hotornot_face aligned_faces

./congealreal/congealReal faces-out.txt image.list
./congealreal/funnelReal faces-out.txt image.list align-out.txt

