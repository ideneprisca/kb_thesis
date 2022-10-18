import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Alex Smith spoke at Sacmi Corp and at Acme Corp last week.")

'''texts = ["Alex Smith ha lavorato presso Sacmi Sarl.",
        "Luca Moretti è nata a Parigi il 21.08.1345"
        "Questa è una frase."]'''
#docs = [nlp(text) for text in texts]
#docs = list(nlp.pipe(texts))
#for doc in nlp.pipe(texts, disable=["tok2vec", "tagger", "parser", "attribute_ruler", "lemmatizer"]):
    #print([(ent.text, ent.label_) for ent in doc.ents])

for token in doc:
    print(token.text, token.dep_, token.head.text , token.head.pos_,
          [child for child in token.children])
'''for tok in doc:
    pass
    print(tok.text, "-->",tok.dep_,"-->", tok.pos_,"-->",tok.tag_)

for ent in doc.ents:
    print(ent.text,ent.label_)'''

person_entities = [ent for ent in doc.ents if ent.label_ == "PERSON"]
for ent in person_entities:
    print(ent)
    # Because the entity is a span, we need to use its root token. The head
    # is the syntactic governor of the person, e.g. the verb
    head = ent.root.head
    print(head)
    if head.lemma_ == "speak":
        # Check if the children contain a preposition
        preps = [token for token in head.children if token.dep_ == "prep"]
        for prep in preps:
            # Check if tokens part of ORG entities are in the preposition's
            # children, e.g. at -> Acme Corp Inc.
            orgs = [token for token in prep.children if token.ent_type_ == "ORG"]
            # If the verb is in past tense, the company was a previous company
            print({"person": ent, "orgs": orgs, "past": head.tag_ == "VBD"})
            result = [ent, head.text, prep]
            print('resr', result)



'''Alex --> nsubj --> PROPN --> SP
Smith --> flat:name --> PROPN --> SP
ha --> aux --> AUX --> VA
lavorato --> ROOT --> VERB --> V
a --> case --> ADP --> E
Acme --> obl --> PROPN --> SP
Corp --> flat:name --> PROPN --> SP
Inc --> flat:name --> PROPN --> SP
. --> punct --> PUNCT --> FS'''


#--------------------------------------------
# #test to locate preposition "a" che funziona
'''for location in location_entities:
    preps = [token for token in doc if token.tag_ == "E"]'''

'''for prep in preps:
        Check if tokens part of ORG entities are in the preposition's
        children, e.g. at -> Acme Corp Inc.
         orgs = [token for token in prep.children if token.ent_type_ == "ORG"]
        If the verb is in past tense, the company was a previous company
         print({"person": ent, "orgs": orgs, "past": head.tag_ == "V"})
    '''

#doc = nlp("De Francisci Gabriele, è nato a Tripoli il 13.10.1954.")

    #print([(ent.text, ent.label_) for ent in doc.ents])
#print(allContent)

#for doc in nlp.pipe(doc, disable=["tok2vec", "tagger", "parser", "attribute_ruler", "lemmatizer"]):

'''De nsubj SP PROPN nato VERB [Francisci, Gabriele, ,]
Francisci flat:name SP PROPN De PROPN []
Gabriele flat:name SP PROPN De PROPN []
, punct FF PUNCT De PROPN []
è aux VA AUX nato VERB []
nato ROOT V VERB nato VERB [De, è, Tripoli, 13.10.1954, .]
a case E ADP Tripoli PROPN []
Tripoli obl SP PROPN nato VERB [a]
il det RD DET 13.10.1954 NUM []
13.10.1954 nummod N NUM nato VERB [il]
. punct FS PUNCT nato VERB []'''

#print  token linguistics features for the sample text of the pattern
'''@:parameter
    token.text, 
    token.dep_, 
    token.tag_,
    token.pos_, 
    token.head.text, 
    token.head.pos_,'''

    #for token in doc:
        #pass
        #print(token.text, token.dep_, token.tag_,token.pos_, token.head.text , token.head.pos_,
              #[child for child in token.children])