337Stuff
========

Playing around with NLP ... for my EECS 337 class. This relies on a file provided by the instructor called 'goldenglobes.json' that I have not included here. The file contains JSON data involving a number of tweets about the 2013 golden globes. The goal of an assignment for the class was to use this data to determine who won each award in the 2013 golden globes. Here I include some scripts and other resources that I used to manipulate, search, categorize this data, etc.

scraper.py : JSON library operations were running slowly on my dual core, so I decided to blame the unnecessary JSON data like date and username, as well as structural things. scraper.py removes this from goldenglobes.json to create scraped.lines, consisting of text only on every line, with no extra data.

normalize.py : sets scraped.lines to be all lower case

unduplicate.py : removes duplicates in scraped.lines, so that each tweet will appear only once (doesn't work if the retweeter added something, like a new tag or the OP's name)

winninglines.py : search for tweets that mention winning or "best". Place them in win.lines. Unfortunately this throws out a lot of good data while retaining some bad data, but it is simple and lowers the overall dataset to a reasonable set.

bigrams.py : preliminary attempt at finding recurring themes across tweets, based on win.lines. It mainly shows that bigrams alone will not be sufficient for extracting all of the data desired from the tweets.

categories.py : a script for trying to separate tweets from win.lines into categories based on categories.lines

categories.lines : a list of categories. Each line contains a single bigram representing a desired category, such as "foreign language" or "best actor."

A typical order of executing the files is scraper.py -> normalize.py -> unduplicate.py -> winninglines.py and then either bigrams.py or categories.py. After categories.py is executed, each file in ./categories/ represents a collection of relevant tweets. This makes a few of the categories very easy (such as lifetime achivement) but does not help with others (since the different types of best actor can not be differentiated using bigrams alone, for example).