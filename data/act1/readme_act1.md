# Activity 1 - Messing around with character n-grams

The python script (`<fasttext-nearest-neighb.py>`) obtains the 10 most similar words with regard to an input item provided through command line.

If the word is in the vocabulary, a word vector is obtained through the word2vec-compatible file (.vec extension). This file only contains: 1) The vocabulary (words and counts); and 2) The vectors for in-vocab words. To load the .vec file, we use the following gensim method: 

`<model_word2vec = gensim.models.Word2Vec.load_word2vec_format(file.vec)>`

If we test an out-of-vocabulary word, we use the fastText .bin model containing also extra information such as vectors of n-grams (if they are computed). This model is loaded through the following gensim method:

`<model_fasttext = fasttext.load_model(fasttext_model.bin)>`
