import sys

fr = open('time.lines', 'r')
time_data = fr.read()
fr.close()
fr = open('scraped.lines', 'r')
text_data = fr.read()
fr.close()
fw = open('timedata.lines', 'w')

ngram = 'poehler'
#ngram = ""
#for arg in sys.argv :
#    if arg != sys.argv[0] :
#        ngram = ngram + arg + " "
#ngram = ngram[:-1]

time_lines = time_data.splitlines()
count = 0
for text_line in text_data.splitlines() :
    if ngram in text_line :
        fw.write(time_lines[count] +'\n')
    count = count + 1

fw.close()
