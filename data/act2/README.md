# Activity 2. Using fastText in a supervised setting

We will use the same set of data from the EMEA corpus, but enriched with labels describing each sentence. 

fastText labels bear the format `__label__` + descriptor:

`__label__treatment mélange des insulines`

The following types of contents were used:

* medical_condition: diseases, symptoms, allergies, presence of bacteria/virus
*	surgery: surgery procedures and anesthesias
*	addiction: alcoholic beverages/habits, toxic drugs, smoking products/habits
*	analysis: medical checkups, examinations and laboratory analysis
*	treatment: medicines, treatments, vaccins, transfusions or healthcare activity
*	physiol: physiological functions
*	medic_dev: medical devices
*	gynec_obstetr: gynecological or obstetric events
*	empty: absence of any of the previous types of topics

Sentences may content different types of topics, each preceded with the `__label__` notation. For example:

`__label__medical_condition __label__treatment  diabète sucré nécessitant un traitement`

**Note that the data were annotated automatically and no revision was done!!**

## 2.1. Train the data

Get the EMEA annotated data.

Full data was split into 2/3 for training and 1/3 for the test:

*	EMEA_part_fr_norm_lbl_ft.trn (train, 5216788 tokens)

*	EMEA_part_fr_norm_lbl_ft.tst (test, 2622677 tokens)

Train using default parameters:

`./fasttext supervised -input EMEA_part_fr_norm_lbl.trn  -output model_EMEA_superv`

`Read 5M words`

`Number of words:  30377`

`Number of labels: 10`

`Progress: 100.0%  words/sec/thread: 2259793  lr: 0.000000  loss: 0.350939  eta: 0h0m`


##2.2. Test the model

 Test the model with the following command (results given in precision and recall; by default, k=1, i.e. precision and recall @1): 

`./fasttext test model_EMEA_superv.bin EMEA_part_fr_norm_u8_nca_ft.tst`

`P@1: 0.957`

`R@1: 0.728`

`Number of examples: 166472`

(this represents roughly an F1-measure of 0.827).

You can also test interactively with the following command (don’t forget the “-“): 

`./fasttext predict test_model_EMEA_superv.bin -`

`je prends de l' aspirine`

`__label__treatment`

`l' aspirine me produit des vomissements`

`__label__medical_condition_treatment`

`j'ai eu une opération`

`__label__surgery`

`je porte de lentilles`

`__label__medic_dev`

## 2.3. Train and test other models and parameters

Other parameters are worth testing: window size, number of word/character n grams, minimum word count, learning rate, negative sampling, number of epochs… Very sophisticated models may take longer to train. 

