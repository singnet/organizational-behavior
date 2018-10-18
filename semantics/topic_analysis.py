# -*- coding: utf-8 -*-
__author__ = 'eyob'
# Tested on python2.7

import psutil
print('rrrrrrrrrrrrrrram used at program start:',float(list(psutil.virtual_memory())[3])/1073741824.0,'GB')

import os
import sys
import pathlib

sys.path.append(str(pathlib.Path(os.path.abspath('')).parents[1])+'/topic-analysis/plsa/plsa')
sys.path.append(str(pathlib.Path(os.path.abspath('')).parents[1])+'/topic-analysis/plsa/preprocessing')

import example_plsa as pplsa
import cleansing_news as pclean

class TopicAnalysis:

    def __init__(self, db):

        self.db = db

        pass

    def __del__(self):

        # Close db connections
        pass








def run_1():

    t = TopicAnalysis('local')


    pass










__end__ = '__end__'


if __name__ == '__main__':

    run_1()

    pass