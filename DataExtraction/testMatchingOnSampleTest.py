from spacy.matcher import Matcher

from docParsing import final, final
import re
import spacy

# load spaCy model
nlp = spacy.load("it_core_news_lg")

# sample text
text_1= "De Francisci Gabriele, imputato di omicidio ed altro."
#text_2 = "De Francisci Gabriele, nato a Tripoli il 13.10.1954."
text_3 = "sei anni"
#how  to create a compound dependence? to take a sentence after anchor predicate


doc = nlp(text_3)

# print token, dependency, POS tag
for tok in doc:
    print(tok.text, "-->",tok.dep_,"-->", tok.pos_)

#pattern's matching creation
#predicato "imputato di"
pattern_1 = [{'POS': 'PROPN', 'OP': "+"},
            {'IS_PUNCT': True, 'OP':'*'},
            {'LOWER': 'imputato'},
            {'LOWER': 'di'},
            {'POS': 'NOUN'}]

#predicato "nato a"
pattern_2 = [{'POS': 'PROPN', 'OP': "+"},
            {'IS_PUNCT': True, 'OP':'*'},
            {'LOWER': 'nato'},
            {'LOWER': 'a'},
            {'POS': 'PROPN'}]

#PHRASE MATCHING
pattern_3 = [{'POS': 'PROPN', 'OP': "+"},
             {'IS_PUNCT': True, 'OP':'*'},
             {'LOWER': 'condannato'},
             {'LOWER': 'a'},
             {'POS': 'NUM'}
]
#condanato a
pattern_3 = [{'POS': 'NUM'},
             {'IS_PUNCT': True, 'OP':'*'},
             {'LOWER': 'condannato'},
             {'LOWER': 'a'},
             {'POS': 'NUM'}
]
#omicidio di
pattern_3 = [
             {'LOWER': 'omicidio'},
             {'LOWER': 'di'},
             {'POS': 'NUM'}
]

matcher = Matcher(nlp.vocab)
matcher.add("matching_2", [pattern_3])
matches = matcher(doc)
for match_id, start, end in matches:
    string_id = nlp.vocab.strings[match_id]  # Get string representation
    span = doc[start:end]  # The matched span
    print("{"+ span.text+"}")