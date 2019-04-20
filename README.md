# Wikipedia Crawler

This python source code simply provides users with basic database
using `requests` and `BeautifulSoup` module. It iterates through
mutable amount of times by jumping into the first `href` link it
finds in the `p` tag of wikipedia web page.

## NLTK Addons
We use nltk database in order to classify each word with its part of speech.
You would need to manually download 'punkt' 'universal_tagset' 'averaged_perceptron_tagger'
with 
`python3 -m nltk.download(`addons-here`)`

## Data format

Word data that is returned in a `cvs` formatted file has three
distintions.
*Word: The actual word from wikipedia paragraph
*Tense: _NOUN_ for nouns, _ADJ_ for adjectives, _VERB_ for verbs, and _NUM_ for numbers
*Path: url path to the wikipedia page where the word was found

## Contact 

If anyone is awesome enough to contact me for any questions revolving around 
this project, feel free to contact me via e-mail **seanhong2000@gmail.com**
You are Awesome
So have a great day!!
