'''
This document contains class function which can process raw string data followed by tokenize, stemming,
lemmatizing and tf-idf vectorizing.
'''

from nltk import word_tokenize
from helpers import *
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

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



    def tokenize(self):
        '''
        Tokeninze the words
        :return: numpy array
        '''
        return np.array([word_tokenize(word) for word in self.words])

    def lower_case(self):
        '''
        lower case bag of words
        :return: numpy array
        '''
        lis = []
        bag = self.tokenize()
        for b in bag:
            lis.append([x.lower() for x in b])
        return np.array(lis)

    def process(self, stem_func):
        '''
        switch all to lower cases, stemming, then lemmatizing
        :param kwargs:
        :return: numpy array, processed training set.
        '''
        lower = self.lower_case()
        stemmed_bag = bag_stemer(stem_func,lower)
        lamma_bag =  bag_lemma(stemmed_bag)
        return join_words(lamma_bag)





