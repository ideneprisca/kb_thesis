import numpy as np
import spacy
from spacy import displacy

from spacyMatcher import docParsing

nlp = spacy.load("it_nerIta_trf")

rootdir = 'C:/Users/user/Desktop/thesis/sestra/bo0144'
allContent = docParsing.listdirs(rootdir)

doc = nlp("Alex Smith è nato a Parigi.")

for k in range(len(allContent)):
    pass
    #doc = nlp(allContent[k])
print([(ent.text, ent.label_) for ent in doc.ents])

# regole relative a al predicato nato

# print token, dependency, POS tag
person_entities = [ent for ent in doc.ents if ent.label_ == "PER"]
for ent in person_entities:
    # Because the entity is a span, we need to use its root token. The head
    # is the syntactic governor of the person, e.g. the verb
    head = ent.root.head
    print(head)
    if head.lemma_ == "nascere":

        # Check if the sentence contain a preposition
        location_entities = [token for token in head.children if token.dep_ == "obl"]
        # print(location_entities)
        for location in location_entities:
            # write result predicate in csv file to transform after in RDF to populate the ontology
            csv_input = [ent, head.text, location]
            print('resr', csv_input)
            csv_input.append(csv_input)
            rows = [csv_input]
            np.savetxt('entry.csv', csv_input, delimiter=',', fmt='% s')


