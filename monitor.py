import time
import hashlib
from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import requests

# Setting the URL you want to monitor
url = "https://conservativebrief.com/"

# Provider request header
headers = {'User-agent': 'Mozilla/5.0'}

request = requests.get(url,headers=headers)
html = request.content

soup = BeautifulSoup(html,'html.parser')

def con_brief_scrapper():
    news_list = []

    for h in soup.findAll("h2",{'class':"post-title"}):
        for i in soup.findChildren("a",recursive=True):
            news_title = i.contents[0]
            if news_title not in news_list:
                news_list.append(news_title)



    for i, title in enumerate(news_list):
        print(i + 1,':',title)


con_brief_scrapper()