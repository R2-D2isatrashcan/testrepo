# -*- coding: utf-8 -*-
import time
import os
from model.prank import Graph, PersonalRank


def run():
    assert os.path.exists('data/ratings.csv'), \
        'File not exists in path, run preprocess.py before this.'
    print('Start..')
    start = time.time()
    if not os.path.exists('data/prank.graph'):
        Graph.gen_graph()
    filename = './data/prank_rec.csv'
    with open(filename, 'wb') as f:
        for i in range(543060):
            PersonalRank().train(user_id=i)
            movies = PersonalRank().predict(user_id=i)
            for movie in movies:
                f.write((str(i)+','+movie+"\n").encode('utf-8'))
            print('Cost time: %f' % (time.time() - start))
