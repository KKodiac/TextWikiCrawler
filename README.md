# Wikipedia Crawler
Source Code for simple wikipedia crawling and keywords extraction.
Using `BeautifulSoup` and `requests`, it scrapes wikipedia with user's requested topic, providing `.txt` with the entire document and `.json` `.csv` for simple data sets of extracted keywords.

</br>
간단한 위키피디아 클롤러와 키워드 선별 소스 코드입니다.
`BeautifulSoup` 과 `requests`를 사용하여 사용자가 원하는 주제를 위키피디아에서 크롤링한 후, `.txt` 파일로 전체 문서를 정리하고, `.json`과 `.csv` 파일로 단어 및 연속된 단어들의 중요도를 정리하여 놓습니다.

## NLTK Addons
We use nltk database in order to classify each word with its part of speech.</br >
Program automatically downloads required NLTK packages </br > 
아래 nltk 라이브러리의 패키지들이 필요합니다.
코드를 실행 시키면 저절로 다운로드 됩니다.
```
punkt
universal_tagset
averaged_perceptroon_tagger
stopwords
```

## Additional Python Libraries Needed
We need following Python Packages</br > 
아래의 파이썬 라이브러리가 필요 합니다.</br>
```
`requests` and
`BeautifulSoup4` for crawling
`rake_nltk` for keyword extraction
```
You can </br > 
위 라이브러리를 다운 받기 위해서는 
```
python3 -m venv ../.env
python3 -m pip install -r requirements.txt
source ../.env/bin/activate
```
to install required python libraries
이렇게 실행 시키시면 됩니다.

## RAKE(Rapid Automatic Keyword Extraction)
For keyword extraction, RAKE algorithm has been used.
For more information regarding RAKE algorithm please go to
[csurfer's](https://github.com/csurfer/rake_nltk) package.
키워드 정리를 위해서 RAKE 알고리즘을 사용했습니다. 
자세한 정보가 필요하면 [csurfer's](https://github.com/csurfer/rake_nltk) 링크를 참고해주세요.

## Contact 

If anyone is interested enough to contact me for any questions revolving around 
this project, feel free to contact me via e-mail **seanhong2000@gmail.com**

