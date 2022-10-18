import spacy
import re
import string

import pandas as pd
import numpy as np
import math

from spacy.matcher import Matcher
from tqdm import tqdm


# load spaCy model
nlp = spacy.load("it_core_news_lg")

# sample text
text = "Tableau è stata recentemente acquisito da Salesforce."
    #"Careem, un'importante società di corse in Medio Oriente, è stata acquisita da Uber."
#"Tableau è stata recentemente acquisito da Salesforce."
# create a spaCy object
doc = nlp(text)

# print token, dependency, POS tag
'''for tok in doc:
    print(tok.text, "-->",tok.dep_,"-->", tok.pos_)'''
#define the pattern
'''pattern_1 = [{'POS': 'DET'},
            {'POS': 'PROPN'},
            {'LOWER': 'continuerà'},
            {'POS': 'ADP'},
            {'POS': 'VERB'}]
           #proper noun
matcher = Matcher(nlp.vocab)
matcher.add("matching_1", [pattern_1])

matches = matcher(doc)
for match_id, start, end in matches:
    string_id = nlp.vocab.strings[match_id]  # Get string representation
    span = doc[start:end]  # The matched span
    print(match_id, string_id, start, end, span.text)'''


def subtree_matcher(doc):
    subjpass = 0

    for i, tok in enumerate(doc):
        # find dependency tag that contains the text "subjpass"
        if tok.dep_.find("subj") == True:
            subjpass = 1

    x = ''
    y = ''

    # if subjpass == 1 then sentence is passive
    if subjpass == 1:
        for i, tok in enumerate(doc):
            if tok.dep_.find("subj") == True:
                y = tok.text

            if tok.dep_.endswith("agent") == True:
                x = tok.text

    # if subjpass == 0 then sentence is not passive
    else:
        for i, tok in enumerate(doc):
            if tok.dep_.endswith("subj") == True:
                x = tok.text

            if tok.dep_.endswith("obj") == True:
                y = tok.text

    return x, y
print(subtree_matcher(doc))

print("sdfghjkjhg")

'''def subtree_matcher(doc):
    x = ''
    y = ''


    # iterate through all the tokens in the input sentence
    for i, tok in enumerate(doc):
        # extract subject
        if tok.dep_.find("subj") == True:
            y = tok.text

            # extract object
        if tok.dep_.endswith("agent") == True:
            x = tok.text

    return x, y'''




