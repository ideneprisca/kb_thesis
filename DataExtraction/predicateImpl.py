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

pattern_1 = [
            {'POS': 'PROPN'},
            {'POS': 'PROPN'},
            {'POS': 'PROPN', 'OP': "*"},
            {'IS_PUNCT': True, 'OP':'*'},
            {'LOWER': 'imputato'},
            {'LOWER': 'di'},
            {'POS': 'NOUN', 'OP': "+"}]

pattern_2 = [{'POS': 'PROPN', 'OP': "+"},
            {'IS_PUNCT': True, 'OP':'*'},
            {'LOWER': 'nato'},
            {'LOWER': 'a'},
            {'POS': 'PROPN'}]

pattern_3 = [{'POS': 'PROPN', 'OP': "+"},
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
matcher.add("matching_1", [pattern_2])

allContent = docParsing.listdirs(rootdir)
#print(allContent)

#regole relative a al predicato nato

# print token, dependency, POS tag
person_entities = [ent for ent in allContent.ents if ent.label_ == "PER"]
for ent in person_entities:
    # Because the entity is a span, we need to use its root token. The head
    # is the syntactic governor of the person, e.g. the verb
    head = ent.root.head
    if head.lemma_ == "rompere":
        # Check if the sentence contain a preposition
        location_entities = [token for token in head.children if token.dep_ == "obl"]
        # print(location_entities)
        for location in location_entities:
            #preps = [token for token in location.children if token.tag_ == "E"]
            #write resul predicate in csv file to transform after in RDF to populate the ontology
            csv_input = [ent, head.text, location]
            print('resr', csv_input)
            csv_input.append(csv_input)
            rows = [csv_input]
            np.savetxt('entry.csv', csv_input, delimiter=',', fmt='% s')



#regole relative a al predicato imputato

person_entities = [ent for ent in allContent.ents if ent.label_ == "PER"]
for ent in person_entities:
    # Because the entity is a span, we need to use its root token. The head
    # is the syntactic governor of the person, e.g. the verb
    head = ent.root.head
    if head.lemma_ == "rompere":
        # Check if the sentence contain a preposition
        location_entities = [token for token in head.children if token.dep_ == "obl"]
        # print(location_entities)
        for location in location_entities:
            #preps = [token for token in location.children if token.tag_ == "E"]
            #write resul predicate in csv file to transform after in RDF to populate the ontology
            csv_input = [ent, head.text, location]
            print('resr', csv_input)
            csv_input.append(csv_input)
            rows = [csv_input]
            np.savetxt('Imputato.csv', csv_input, delimiter=',', fmt='% s')





#csv file writing with pattern matcher
'''csv_input = []
for k in range(len(allContent)):
    doc = nlp(allContent[k])
    matches = matcher(doc)
    if len(matches) != 0:
        for match_id, start, end in matches:
            string_id = nlp.vocab.strings[match_id]  # Get string representation
            span = doc[start:end]  # The matched span
            result = span.text
            csv_input.append(result)
rows = [csv_input]
np.savetxt('datas.csv', csv_input, delimiter=' ', fmt ='% s')'''





