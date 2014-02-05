import nltk
fw = open("win.lines", "r")
read_data = fw.read()
fw.close()
data_tokens = nltk.word_tokenize(read_data)
data_bigrams = nltk.bigrams(data_tokens)
data_fdist = nltk.FreqDist(data_bigrams)
for k, v in data_fdist.items() :
    if v > 100 :
        print k, v
