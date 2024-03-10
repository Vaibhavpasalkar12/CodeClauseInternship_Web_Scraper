from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def news_headline(url):
    res = requests.get(url)
    if res.status_code == 200:
        BS = BeautifulSoup(res.text, 'html.parser')
        news_headline = BS.find_all('h1', itemprop="headline")
        headlines = [headline.text.strip() for headline in news_headline]
        return headlines
    else:
        return None

@app.route('/')
def index():
    url = request.args.get('url')
    headlines = news_headline(url) if url else None
    return render_template('index.html', headlines=headlines)

if __name__ == '__main__':
    app.run(debug=True)
