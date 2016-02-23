'''
This documents contains helper functions
'''
import numpy as np
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer

def bag_stemer(stem_func,bag):
    '''
    stemming bag of words
    :param stem_func: string, stemmer method, "porter" or "snowball"
    :param bag: numpy array, bag of words
    :return: np.array
    '''
    if stem_func == "porter":
        stemmer = PorterStemmer()
    elif stem_func == "snowball":
        stemmer = SnowballStemmer()
    else:
        return "Wrong input. please put 'porter' or 'snowball'"
    stem_lis = []
    for b in bag:
        stem_lis.append([stemmer.stem(x.decode('utf-8')) for x in b])
    return np.array(stem_lis)

def bag_lemma(bag):
    '''
    lemmatize bag of words
    :param bag:numpy array, bag of words
    :return: np.array
    '''
    wnl = WordNetLemmatizer()
    lemma_lis =[]
    for b in bag:
        lemma_lis.append([wnl.lemmatize(x) for x in b])
    return np.array(lemma_lis)

