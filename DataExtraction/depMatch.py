from spacy.matcher import DependencyMatcher
import  spacy
nlp = spacy.load(en_core_web_sm)

# "[subject] ... initially founded"
pattern = [
  # anchor token: founded
  {
    "RIGHT_ID": "founded",
    "RIGHT_ATTRS": {"ORTH": "founded"}
  },
  # founded -> subject
  {
    "LEFT_ID": "founded",
    "REL_OP": ">",
    "RIGHT_ID": "subject",
    "RIGHT_ATTRS": {"DEP": "nsubj"}
  },
  # "founded" follows "initially"
  {
    "LEFT_ID": "founded",
    "REL_OP": ";",
    "RIGHT_ID": "initially",
    "RIGHT_ATTRS": {"ORTH": "initially"}
  }
]

matcher = DependencyMatcher(nlp.vocab)
matcher.add("FOUNDED", [pattern])
matches = matcher(doc)