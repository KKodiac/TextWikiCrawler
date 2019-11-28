# Created while doing mendatory military service in ROKArmy GOP Unit
# This branch has removed Web Integration
# Wikipedia Crawler

This python source code simply provides users with basic database
using `requests` and `BeautifulSoup` module. It iterates through
mutable amount of times by jumping into the first `href` link it
finds in the `p` tag of wikipedia web page.
I'm trying to work on a language processing program by applying 
Machine Learning to it from scratch. 

## NLTK Addons
We use nltk database in order to classify each word with its part of speech.
You would need to manually download 
`punkt`
`universal_tagset`
`averaged_perceptron_tagger`
with 
`python3 -m nltk.download([addons-here])`


## Additional Modules Needed
We need 
`requests` and
`BeautifulSoup4` for crawling
`pandas` for language processing 

## Data format

Word data that is returned in a `cvs` formatted file has three
distintions.
*Word: The actual word from wikipedia paragraph
*Tense: _NOUN_ for nouns, _ADJ_ for adjectives, _VERB_ for verbs, and _NUM_ for numbers
*Path: url path to the wikipedia page where the word was found

## Notes
From django framework, will be working on Notes creater that automatically create notes involving a topic that
a user desires.


## Contact 

If anyone is interested enough to contact me for any questions revolving around 
this project, feel free to contact me via e-mail **seanhong2000@gmail.com**

