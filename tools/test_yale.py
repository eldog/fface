#!/usr/bin/env python2.7
import eigenface

data = eigenface.data_from_dir('test')
eig = eigenface.EigFace()
eig.create_eig_faces(data)
