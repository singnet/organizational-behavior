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


def test_preprocessing():

    root_folder = str(pathlib.Path(os.path.abspath('')).parents[1])+'/appData/'

    pclean.file_parts_number=9
    pclean.file_dict = root_folder + 'plsa/dict/test_dict'
    pclean.source_texts = root_folder + 'plsa/extracted/*.txt'
    pclean.output_dir = root_folder + 'plsa/cleaned/'


    # Do cleansing on the data and turing it to bad-of-words model
    pclean.pre_pro()

    # Train using PLSA
    pplsa.folder = pclean.output_dir[:-1]
    pplsa.dict_path = pclean.file_dict
    pplsa.folder = root_folder + 'plsa/cleaned'
    pplsa.main()









__end__ = '__end__'


if __name__ == '__main__':

    # run_1()
    test_preprocessing()

    pass