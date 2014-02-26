from pylab import *

fr = open('timedata.lines', 'r')
read_data = fr.read()
fr.close()
read_lines = read_data.splitlines()

num_lines = []
for line in read_lines :
    num_lines.append((int(line) / 1000 - 1358124338) / 60 )

figure()
hist(num_lines, 20)
ylabel('Number of tweets containing ngram in timerange')
xlabel('Time since first tweet, in minutes')
show()
