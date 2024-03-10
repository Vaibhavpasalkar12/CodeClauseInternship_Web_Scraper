import requests
from bs4 import BeautifulSoup

def news_headline(url):
    res = requests.get(url)
    if res.status_code==200:
        BS=BeautifulSoup(res.text, 'html.parser')
        news_headline=BS.find_all('h1', itemprop="headline")
        headlines=[headline.text.strip() for headline in news_headline]
        return headlines
    else:
        print('Failed')
        return None

url = 'https://indianexpress.com/article/india/kerala-govt-cbi-probe-death-veterinary-student-wayanad-9204562/'

headlines=news_headline(url)

if headlines:
    for i, headline in enumerate(headlines, start=1):
        print(f'{i}. {headline}')
else:
    print('Not found')
