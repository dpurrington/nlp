from nltk.corpus import gutenberg
import nltk
# nltk.download('gutenberg')
#nltk.download('punkt')
from pprint import pprint
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktTrainer
from nltk.corpus import gutenberg
import nltk.data
sent_detector = nltk.data.load("tokenizers/punkt/english.pickle")

text = ""
for file_id in gutenberg.fileids():
    text += gutenberg.raw(file_id)

#trainer = PunktTrainer()
#trainer.INCLUDE_ALL_COLLOCS = True
#trainer.train(text)

#tokenizer = PunktSentenceTokenizer(trainer.get_params())
tokenizer = sent_detector
# Test the tokenizer on a piece of text
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
