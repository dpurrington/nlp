from nltk.corpus import gutenberg
import nltk
# nltk.download('gutenberg')
from pprint import pprint
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktTrainer

text = ""
trainer = PunktTrainer()
trainer.INCLUDE_ALL_COLLOCS = True
trainer.train(text)

tokenizer = PunktSentenceTokenizer(trainer.get_params())

# Test the tokenizer on a piece of text
sentences = "Mr. James told me Dr. Brown is not available today. I will try tomorrow."
tokenizer._params.abbrev_types.add('dr')
tokenizer._params.abbrev_types.add('mr')

f = open("transcript.txt", "r")
input_text = f.read()
input_text = input_text.replace("\nRobert", " ")
input_text = input_text.replace("\nLara", " ")
input_text = input_text.replace("\n", " ")
sentences = tokenizer.tokenize(input_text)

# TODO: rejoin where sentence starts with lower case

sfile = open("sentences.txt", "w")
for s in sentences:
    sfile.write(s + "\n")

questions = [q for q in sentences if q.endswith("?") and "[inaudible]" not in q]

qfile = open("questions.txt", "w")
for q in questions:
    qfile.write(q + "\n")
