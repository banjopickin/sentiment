'''
This document contains class function which can process raw string data followed by tokenize, stemming,
lemmatizing and tf-idf vectorizing.
'''

from nltk import word_tokenize
from helpers import *
import numpy as np

class word_processor(object):
    '''
    This class function process string array.
    '''
    def __init__(self, data, str_ind):
        '''

        :param data: numpy array
        :param str_ind: int, indicate which column of data contains strings
        :return: None
        '''
        self.data = data
        self.words = data[:,str_ind]
        self.fin_data = None

    def tokenize(self):
        '''
        Tokeninze the words
        :return: numpy array
        '''
        self.bag = np.array([word_tokenize(word) for word in self.words])

    def stemming(self,stem_func):
        '''
        stemmer
        :param stem_func: string. "snowball" or "porter"
        :return: numpy array
        '''
        self.stemed_bag = bag_stemer(stem_func,self.bag)

    def lemmatize(self):
        '''
        lemmatize strings
        :return: numpy array
        '''

