#
# -*- coding: UTF-8 -*-
# fasttext-nearest-neighb.py
#
# L. Campillos, 2017
#
###########################

import re
import sys
import os
import fasttext
import numpy as np

#os.chdir('./Library/Python/2.7/site-packages/gensim-0.13.2-py2.7-macosx-10.11-intel.egg/gensim')

# To see logging events
import gensim
from collections import defaultdict
from gensim import corpora
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#### subroutines

# Initialize a model (data, vector size, window size, minimum count, workers (threads?))
# Load already compiled model from binary (compiled with C word2vec)
model_word2vec = gensim.models.Word2Vec.load_word2vec_format('./EMEA_part_fr_ws1_4-8chgr_dim100_neg10.vec')
model_fasttext = fasttext.load_model('./EMEA_part_fr_ws1_4-8chgr_dim100_neg10.bin')

print("Model loaded...")

# For testing from input
while True:
    #new_words = raw_input("Enter input word (CTRL+D to quit):\n") # python 2
    new_word = input("Enter input word (CTRL+D to quit):\n")
    if new_word:
        test = None
        try:
            # NEAREST NEIGHBORS
            new_word = new_word.lower()
            #word_vector = model_word2vec[new_word]
            #print(word_vector) # Prints the word vector
            test = model_word2vec.most_similar(new_word)
            #print(len(model_word2vec[new_word])) #Prints the word vector length
        except:
            print("Word not in corpus!")
            # When an out-of-vocabulary word, returns a non-zero vector of n-dimension from the FastText model:
            word_vector = model_fasttext[new_word.lower()]
            #print(len(word_vector)) #Prints the vector dimension
            vector = np.array(word_vector,dtype='f')
            test = model_word2vec.most_similar( [ vector ], topn=10)
        if test!=None:
            # Sort and print 10 words from nearest to furthest item
            sorted_list = sorted(enumerate(test), key=lambda item: item[0])
            for k, v in sorted_list:
                print(v)
            pass
        else:
            print("Try with another word")