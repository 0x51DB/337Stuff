# should create new files for each category
import os
if not os.path.exists('./categories') :
    os.makedirs('./categories')

fr = open('win.lines','r')
read_data = fr.read()
fr.close()

import nltk
fw = open('./categories/bestdirector.lines','w')
for line in read_data.splitlines() :
    read_tokens = nltk.word_tokenize(line)
    read_bigrams = nltk.bigrams(read_tokens)
    if ("best", "director") in read_bigrams :
        fw.write(line)

fw.close()
