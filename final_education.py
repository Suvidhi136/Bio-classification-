#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 14:59:00 2018

@author: rishabhshetty
"""
## This code only gives institutions inorder of bchelors and masters
import pandas as pd
import spacy
import numpy as np
import re

from nltk import sent_tokenize, word_tokenize, pos_tag, ne_chunk
import string
nlp = spacy.load('en_core_web_sm')
data = pd.read_csv('Bioclassification.csv')
bio = data.Biography

## Cleans the string and gets rid of the extra fullstops, converts P.hd -> phd and so on ....
def string_cleaner(sentence):
    S = sentence
    S = S.replace('M.A.', 'Masters')
    S = S.replace('B.S.EE', 'Bachelors')
    S = S.replace('BSEE', 'Bachelors')
    S = S.replace('B.S.F.S.', 'Bachelors')
    S = S.replace('B.B.A.', 'Bachelors')
    S = S.replace('B.B.A.', 'Bachelors')
    S = S.replace('B.S.E.E.', 'Bachelors')
    S = S.replace('M.S.E.E.', 'Masters')
    S = S.replace('B.S.E.', 'Bachelors')
    S = S.replace('bachelor’s', 'Bachelors')
    S = S.replace("bachelor's", 'Bachelors')
    S = S.replace('Master', 'Masters')
    S = S.replace('M.B.A.', 'Masters')
    S = S.replace('B.S.', 'Bachelors')
    S = S.replace('B.A.', 'Bachelors')
    S = S.replace('Ph.D.', 'Masters')
    S = S.replace('MBA', 'Masters')
    S = S.replace('LLB', 'Bachelors')
    S = S.replace('undergraduate', 'Bachelors')
    S = S.replace('M.D.', 'Masters')
    S = S.replace('M.S.', 'Masters')
    S = S.replace('B.Sc.', 'Bachelors')
    S = S.replace("Bachelors's", 'Bachelors')
    S = S.replace('Masterss', 'Masters')
    S = S.replace('BA', 'Bachelors')
    S = S.replace('BS', 'Bachelors')
    S = S.replace('MS', 'Masters')
    return(S)

#def string_cleaner(sentence):
#    S = sentence 
#    S = re.sub(r'\bM.A.\b', 'Masters', S)
#    S = re.sub(r'\bMaster\b', 'Masters', S)
#    S = re.sub(r'\bM.B.A.\b', 'Masters', S)
#    S = re.sub(r'\bmaster\b', 'Masters', S)
#    S =re.sub(r'\bMBA\b', 'Masters', S)
#    S =re.sub(r'\bM.D.\b', 'Masters', S)
#    S =re.sub(r'\bB.sc.\b', 'Bachelors', S)
#    S =re.sub(r'\bBachelor\b', 'Bachelors', S)
#    S =re.sub(r'\B.S.E.\b', 'Bachelors', S)
#    S =re.sub(r'\bB.S.\b', 'Bachelors', S)
#    S =re.sub(r'\bbachelor\b', 'Bachelors', S)
#    S =re.sub(r'\bB.A.\b', 'Bachelors', S)
#    S =re.sub(r'\bLLB\b', 'Bachelors', S)
#    S =re.sub(r'\bundergraduate\b', 'Bachelors', S)
#    return(S)




## Cleans the bio after running the function 
final_bio = []
    
for i in range(len(bio)):
    final_bio.append(string_cleaner(bio[i]))
    


### Gets the educational institites out of the sentence in the form of a list 
def educational_finder(sentence):
    the_org_list = []
    nlp_sent = nlp(sentence)
    for orgs in nlp_sent.ents:
        if orgs.label_ == 'ORG' and ('University' in str(orgs) or 'School' in str(orgs) or 'College' in str(orgs)):
            the_org_list.append(orgs)
    return(the_org_list)

## Gets only the important sentences from the whole paragraph, Seperate for masters and bachelors.
def important_sent(sentence):
    S= {}
    sent = sent_tokenize(sentence)
    for each_sent in sent:
        if 'BACHELORS' in each_sent.upper() and 'MASTERS' not in each_sent.upper():
            S['Bachelors'] = each_sent
        elif 'MASTERS' in each_sent.upper() and 'BACHELORS' not in each_sent.upper():
            S['Masters'] = each_sent
        elif 'BACHELORS' in each_sent.upper() and 'MASTERS' in each_sent.upper():
            S['Both'] = each_sent
        elif 'GRADUATED' in each_sent.upper():
            S['Bachelors'] = each_sent
        elif 'GRADUATE' in each_sent.upper():
            S['Bachelors'] = each_sent
    return(S)

## Depending on the type of sentence it returns a list in the form [Bachelors, masters] and   
## if they have len 3 include the middle one in other educations          
def education_both(sentence):
    words = word_tokenize(sentence)
    list_edu = []
    for i in range(len(words)):
        if words[i].upper() == "BACHELORS" or words[i].upper() == 'GRADUATED' or words[i].upper() == 'PASSED' or words[i].upper() == 'GRADUATE':
            list_edu = educational_finder(sentence)
            return list_edu
        if words[i].upper() == "MASTERS":
            list_edu = educational_finder(sentence)
            list_edu.reverse()
            return list_edu
        
        

final_bio = final_bio    
###looping through the whole list
final_list = []
for bios in final_bio:
    education_list = []
    important = important_sent(bios)
    try:
        if important['Bachelors'] != [] and education_both(important['Bachelors']) != None:
            education_list +=education_both(important['Bachelors'])
    except KeyError:
        pass
    
    try:
        if important['Masters'] != [] and education_both(important['Masters']) != None:
           education_list +=education_both(important['Masters'])
    except KeyError:
        pass
    
    try:
        if important['Both'] != []:
            single_college = education_both(important['Both'])
            try:
                if len(single_college) == 1:
                    single_college.append(single_college[0])
                    education_list += single_college
                else:
                    education_list +=single_college
            except TypeError:
                pass
    except KeyError:
        pass
    final_list.append(education_list)

# Correction for harvard Business school 
    
for row in final_list:
    try:
        if row[0]:
            x = str(row[0])
            y = x.upper()
        if 'BUSINESS' in y and 'HARVARD' in y:
            try:
                row[0],row[1] = row[1],row[0]
            except IndexError:
                pass
    except IndexError:
        pass
    

    

 



                    

    