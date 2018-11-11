#!/usr/bin/env python

import nltk
import nltk.data
tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")
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

rejoined = []
for i, _ in enumerate(sentences):
    print(rejoined)
    print(sentences[i])
    if not sentences[i][0].islower():
        rejoined.append(sentences[i])
    else:
        rejoined[-1] = rejoined[-1] + sentences[i]

questions = [q for q in rejoined if q.endswith("?")
             and "[inaudible]" not in q]


qfile = open("questions.txt", "w")
for q in questions:
    qfile.write(q + "\n")
