#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 10:54:47 2018

@author: rishabhshetty
"""
## Importing all the important libraries
import pandas as pd
import spacy
import numpy as np

from nltk import sent_tokenize, word_tokenize, pos_tag, ne_chunk
import string
nlp = spacy.load('en_core_web_sm')
data = pd.read_csv('Bioclassification.csv')
bio = data.Biography

## Stirng cleaner for replacement of words.

def string_cleaner(sentence):
    S = sentence
    S = S.replace('M.A.', 'MA')
    S = S.replace('MBA', 'Masters')
    S = S.replace('BA', 'Bachelors')
    S = S.replace('Bachelor', 'Bachelors')
    S = S.replace('graduated', 'Bachelors')
    S = S.replace('bachelor', 'Bachelors')
    S = S.replace('B.S.EE', 'Bachelors')
    S = S.replace('B.S.F.S.', 'Bachelors')
    S = S.replace('B.B.A.', 'Bachelors')
    S = S.replace('B.S.E.E.', 'Bachelors')
    S = S.replace('M.S.E.E.', 'MSEE')
    S = S.replace('M.Sc.', 'MSC')
    S = S.replace('B.S.E.', 'Bachelors')
    S = S.replace('bachelor’s', 'Bachelors')
    S = S.replace("bachelor's", 'Bachelors')
    S = S.replace('Master', 'Masters')
    S = S.replace('M.B.A.', 'MBA')
    S = S.replace('B.S.', 'Bachelors')
    S = S.replace('B.A.', 'Bachelors')
    S = S.replace('Ph.D.', 'PHD')
    S = S.replace('LLB', 'Bachelors')
    S = S.replace('undergraduate', 'Bachelors')
    S = S.replace('M.D.', 'MD')
    S = S.replace('M.S.', 'MS')
    S = S.replace('B.Sc.', 'Bachelors')
    S = S.replace("Bachelors's", 'Bachelors')
    S = S.replace('Masterss', 'Masters')

    return(S)
    
## Data cleaned that is without any bachlors or masters 
def Cleaner_rev(sentence):
    clean_bio = ''
    sents = sent_tokenize(sentence)
    for i in sents:
        if 'BACHELORS' in i.upper() or 'MASTERS'in i.upper() or 'COLLEGE' in i.upper():
            pass
        else:
            clean_bio+= i
        
    return(clean_bio)

## Looping through data to get clean useful data.
usable_bio = []
for bios in bio:
    new_bio = Cleaner_rev(string_cleaner(bios))
    usable_bio.append(new_bio)