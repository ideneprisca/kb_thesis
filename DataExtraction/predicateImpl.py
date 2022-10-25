import re
import spacy
import docParsing
from spacy.matcher import Matcher
import csv
import numpy as np

rootdir = 'C:/Users/user/Desktop/thesis/sestra/bo0144'

# load spaCy model
nlp = spacy.load("it_core_news_lg")

#pattern's matching creation

#imputato_di
pattern_1 = [{'POS': 'PROPN', 'OP': "+"},
            {'ENT_TYPE': 'PER'},
            {'IS_PUNCT': True, 'OP':'*'},
            {'LOWER': 'imputato'},
            {'LOWER': 'di'},
            {'POS': 'NOUN', 'OP': "+"}]

#nato_a
pattern_2 = [{'POS': 'PROPN', 'OP': "+"},
            {'ENT_TYPE': 'PER'},
            {'IS_PUNCT': True, 'OP':'*'},
            {'LOWER': 'nato'},
            {'LOWER': 'a'},
            {'ENT_TYPE': 'LOC'}]
#nato_il
pattern_nato_il = [{'POS': 'PROPN', 'OP': "+"},
            {'ENT_TYPE': 'PER'},
            {'IS_PUNCT': True, 'OP':'*'},
            {'LOWER': 'nato'},
            {'LOWER': 'a'},
            {'ENT_TYPE': 'LOC'},
            {'LOWER': 'il'},
            {'POS': 'NUM'}]
#Condannat_a
pattern_3 = [{'POS': 'PROPN', 'OP': "+"},
            {'ENT_TYPE': 'PER'},
             {'IS_PUNCT': True, 'OP':'*'},
             {'LOWER': 'condannato'},
             {'LOWER': 'a'},
             {'POS': 'NUM'},
             {'POS': 'NOUN', 'OP': "+"}
]
#omicidio di
pattern_4 = [
             {'LOWER': 'omicidio'},
             {'LOWER': 'di'},
             {'POS': 'PROPN', 'OP': "+"}
]

matcher = Matcher(nlp.vocab)
matcher.add("matching_1", [pattern_nato_il])
result = []
csv_input = []

#loading xml file in directory
allContent = docParsing.listdirs(rootdir)
#print(allContent)
#read all page tag content extract from xml file
for k in range(len(allContent)):
    doc = nlp(allContent[k])
    matches = matcher(doc)
    if len(matches) != 0:
        for match_id, start, end in matches:
            string_id = nlp.vocab.strings[match_id]  # Get string representation
            span = doc[start:end]  # The matched span
            result = span.text
            #print(type(result))
            doc2 = nlp(span.text)
            model = [(ent.text) for ent in doc2.ents]
            csv_input.append(model)
    rows = [csv_input]
    np.savetxt('Imputato_di.csv', csv_input, delimiter=',', fmt='% s')


            #print([(ent.text, ent.label_) for ent in doc2.ents])
            #print([(ent.text, ent.label_) for ent in doc2.ents if (ent.label_== "PER")])










