import numpy as np
import spacy
from spacy import displacy

from spacyMatcher import docParsing

nlp = spacy.load("it_core_news_lg")
rootdir = 'C:/Users/user/Desktop/thesis/sestra/bo0144'
allContent = docParsing.listdirs(rootdir)
#print(allContent)

doc = nlp("Alex Smith è nato a Parigi.")
##print(doc)

#for k in range(len(allContent)):
'''texts = allContedocnt
for doc in nlp.pipe(texts):'''
print([(ent.text, ent.label_) for ent in doc.ents])

'''for token in doc:
   print(token.text, token.dep_,token.tag_, token.head.text, token.head.pos_,
              [child for child in token.children])'''

person_entities = [ent for ent in doc.ents if ent.label_ == "PER"]
for ent in person_entities:
    # Because the entity is a span, we need to use its root token. The head
    # is the syntactic governor of the person, e.g. the verb
    head = ent.root.head
    print(head)

csv_input = []
result = []

#print(person_entities)
'''for ent in person_entities:
    print(ent)
    # Because the entity is a span, we need to use its root token. The head
    # is the syntactic governor of the person, e.g. the verb
    head = ent.root.head
    #print("-----------", head.lemma_)
    if head.lemma_ == "rompere":
        #print("entr")
        #print("-----------",head.lemma_)
        # Check if the sentence contain a preposition
        location_entities = [token for token in head.children if token.dep_ == "obj"]
        location_entities2 = [token for token in head.children if token.ent_type_ == "ORG"]

        # print(location_entities)
        print('-------------',location_entities)
        for location, loca in enumerate(location_entities,len(location_entities2)):
            #preps = [token for token in location.children if token.tag_ == "E"]
            #print(preps)
            #print({"person": ent, "orgs": location, "past": head.tag_ == "V"})
            result = [ent, head.text, location]
            result2 = [ent, head.text, loca]

            print('resr', result)
            print('resr22', result2)


            csv_input.append(result)
            rows = [csv_input]
            np.savetxt('entry.csv', csv_input, delimiter=',', fmt ='% s')'''