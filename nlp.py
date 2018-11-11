#!/usr/bin/env python
import sys
import nltk
import nltk.data

input_file = sys.argv[1]
tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")
tokenizer._params.abbrev_types.add('dr')
tokenizer._params.abbrev_types.add('mr')

f = open(input_file, "r")
input_text = f.read()
# replace the name labels, this can be done differently with
# a differently-formatted transcript
input_text = input_text.replace("\nRobert", " ")
input_text = input_text.replace("\nLara", " ")
input_text = input_text.replace("\n", " ")
sentences = tokenizer.tokenize(input_text)

# sfile = open("sentences.txt", "w")
# for s in sentences:
#    sfile.write(s + "\n")

rejoined = []
# the tokenizer splits on some things it shouldn't. We assume
# the capitalization is correct, so we go through and rejoin
# lines that begin with a lower case letter back to the prior
# line.
for i, _ in enumerate(sentences):
    if i == 0 or not sentences[i][0].islower():
        rejoined.append(sentences[i])
    else:
        rejoined[-1] = rejoined[-1] + sentences[i]

# questions end with a question mark. Exclude inaudible.
questions = [q for q in rejoined if q.endswith("?")
             and "[inaudible]" not in q]

# qfile = open("questions.txt", "w")
for q in questions:
    print (q + '\n')
    # qfile.write(q + "\n")
