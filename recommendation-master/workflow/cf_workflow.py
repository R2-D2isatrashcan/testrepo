# -*- coding: utf-8 -*-
import time
import os
from model.cf import UserCf


def run():
    print('Start..')
    start = time.time()
    movies = UserCf().calculate()
    for movie in movies:
        print(movie)
    print('Cost time: %f' % (time.time() - start))
