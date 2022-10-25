import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Alex Smith worked at Acme Corp Inc.")
for tok in doc:
    print(tok.text, "-->",tok.dep_,"-->", tok.pos_)
print([(ent.text, ent.label_) for ent in doc.ents])
person_entities = [ent for ent in doc.ents if ent.label_ == "PERSON"]
for ent in person_entities:
    # Because the entity is a span, we need to use its root token. The head
    # is the syntactic governor of the person, e.g. the verb
    head = ent.root.head
    if head.lemma_ == "work":
        # Check if the children contain a preposition
        preps = [token for token in head.children if token.dep_ == "prep"]
        print(preps)
        for prep in preps:
            # Check if tokens part of ORG entities are in the preposition's
            # children, e.g. at -> Acme Corp Inc.
            orgs = [token for token in prep.children if token.ent_type_ == "ORG"]
            # If the verb is in past tense, the company was a previous company
            print({"person": ent, "orgs": orgs, "past": head.tag_ == "VBD"})
