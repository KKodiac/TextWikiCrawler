# Created while doing mendatory military service in ROKArmy GOP Unit</br > 군대에서 현타 올 때 만들었어용
# This branch has removed Web Integration
# Wikipedia Crawler

This python source code simply provides users with basic database
using `requests` and `BeautifulSoup` module. It iterates through
mutable amount of times by jumping into the first `href` link it
finds in the `p` tag of wikipedia web page.
I'm trying to work on a language processing program by applying 
Machine Learning to it from scratch. 

## NLTK Addons
We use nltk database in order to classify each word with its part of speech.</br > 
Program automatically downloads required NLTK packages </br > 
```
punkt
universal_tagset
averaged_perceptroon_tagger
stopwords
```

## Additional Python Libraries Needed
We need </br > 
```
`requests` and
`BeautifulSoup4` for crawling
`pandas` for language processing 
```
You can </br > 
```
python3 -m pip install -r requirements.txt
```
to install required python libraries

## Data format

Word data that is returned in a `cvs` formatted file has three
distintions.
*Word: The actual word from wikipedia paragraph
*Tense: _NOUN_ for nouns, _ADJ_ for adjectives, _VERB_ for verbs, and _NUM_ for numbers
*Path: url path to the wikipedia page where the word was found


## Contact 

If anyone is interested enough to contact me for any questions revolving around 
this project, feel free to contact me via e-mail **seanhong2000@gmail.com**

