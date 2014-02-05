337Stuff
========

Playing around with NLP ... for my EECS 337 class

scraper.py : JSON library operations were running slowly on my dual core, so I decided to blame the unnecessary JSON data like date and username, as well as structural things. scraper.py removes this from goldenglobes.json to create scraped.lines, consisting of text only on every line, with no extra data.

normalize.py : sets scraped.lines to be all lower case

unduplicate.py : removes duplicates in scraped.lines, so that each tweet will appear only once (doesn't work if the retweeter added something, like a new tag or the OP's name)

winninglines.py : search for tweets that mention winning or "best". Place them in win.lines

bigrams.py : preliminary attempt at finding recurring themes across tweets, based on win.lines
