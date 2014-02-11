# should create new files for each category
import os
import shutil
if os.path.exists('./categories') :
    shutil.rmtree('./categories')
os.makedirs('./categories')

fr = open('win.lines','r')
read_data = fr.read()
fr.close()
read_lines = read_data.splitlines()

import nltk
fr = open('categories.lines', 'r')
categories_data = fr.read()
fr.close()
categories_lines = categories_data.splitlines()

for cline in categories_lines :
    cattemp = cline.split()
    file_name = './categories/' + cattemp[0] + cattemp[1] + '.lines'
    category = (cattemp[0], cattemp[1])
    fw = open(file_name,'w')

    for rline in read_lines :
        read_tokens = nltk.word_tokenize(rline)
        read_bigrams = nltk.bigrams(read_tokens)
        if category in read_bigrams :
            fw.write(rline + '\n')

    fw.close()
