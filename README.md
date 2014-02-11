337Stuff
========

Playing around with NLP ... for my EECS 337 class

scraper.py : JSON library operations were running slowly on my dual core, so I decided to blame the unnecessary JSON data like date and username, as well as structural things. scraper.py removes this from goldenglobes.json to create scraped.lines, consisting of text only on every line, with no extra data.

normalize.py : sets scraped.lines to be all lower case

unduplicate.py : removes duplicates in scraped.lines, so that each tweet will appear only once (doesn't work if the retweeter added something, like a new tag or the OP's name)

winninglines.py : search for tweets that mention winning or "best". Place them in win.lines. Unfortunately this throws out a lot of good data while retaining some bad data, but it is simple and lowers the overall dataset to a reasonable set.

bigrams.py : preliminary attempt at finding recurring themes across tweets, based on win.lines. It mainly shows that bigrams alone will not be sufficient for extracting all of the data desired from the tweets.

categories.py : this may turn out to be quite useless. The idea was to use this as the basis for a script that classifies tweets according to the award they refer to using bigrams. The main problems are that not all tweets are explicit about their categories (example tweet: 'adele skyfall wins') and the awards themselves can not be broken up based on bigrams alone - there are multiple best actors and actresses, for example. Using larger ngrams, however, would also be unreasonable, since a tweet is unlikely to spell out 'best actor in a comedy or musical,' for example.

A typical order of executing the files is scraper.py -> normalize.py -> unduplicate.py -> winninglines.py and then either bigrams.py or categories.py.