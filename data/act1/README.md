# Activity 1 - Messing around with character n-grams

The python script (`fasttext-nearest-neighb.py`) obtains the 10 most similar words with regard to an input item provided through command line.

If the word is in the vocabulary, a word vector is obtained through the word2vec-compatible file (.vec extension). This file only contains: 1) The vocabulary (words and counts); and 2) The vectors for in-vocab words. To load the .vec file, we use the following gensim method: 

`model_word2vec = gensim.models.Word2Vec.load_word2vec_format(file.vec)`

If we test an out-of-vocabulary word, we use the fastText .bin model containing also extra information such as vectors of n-grams (if they are computed). This model is loaded through the following gensim method:

`model_fasttext = fasttext.load_model(fasttext_model.bin)`

## Act. 1.1. Exploring the effect of character n-grams

### 1.1.1. Train and load a model without character n-grams

`EMEA_part_fr_ws10_0chgr_dim100_neg10`

`EMEA_part_fr_ws1_0chgr_dim100_neg10`

Data is a subset of the French corpus from the European Medicines Agency (>7M tokens). The full data can be get at: http://opus.lingfil.uu.se/EMEA.php 
Both models were trained with minimum word count of 1, vector dimension of 100, negative sampling of 10, and learning rate of 0.05 (default value in fastText).

First test with words that might be found in the vocabulary: e.g. *aspirine, hypertension, hépatique, distal*. 
Notice the results that you get.

Then try again with another model with a different window size than that tested before. Note if you get a different output.

### 1.1.2. Train and load a model with character n-grams

Load any of the following models trained with character n-grams (min.: 4; max.: 8) and the same configuration as the previous ones (except window size):

`EMEA_part_fr_ws10_4-8chgr_dim100_neg10`

`EMEA_part_fr_ws1_4-8chgr_dim100_neg10`

Try out-of-vocabulary words: e.g. spelling mistakes (&ast;*adpirine*, &ast;*colioscopie*), commercial names (&ast;*nintédanib*).  Compare the output.

## Act. 1.2. Exploring the effect of window size

Load any of the previous models and compare it with the corresponding pair with a different window size. 

Try only in-vocabulary words and notice which types of words you get. 
Analyze the POS-categories, derivation variants, acronyms or synonyms.

## Other remarks

So far we have only tested 2 training parameters. When working with a big corpus, the parameter of minimum word count might be increased to rule out very low frequency items such as spelling mistakes, tokenization problems or hapax (rare words occurring 1 time). 





