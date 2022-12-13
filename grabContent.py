from bs4 import BeautifulSoup
import requests




# Provider request header
headers = {'User-agent': 'Mozilla/5.0'}



def con_brief_scrapper():
    # Setting the URL you want to monitor
    urlOne = "https://conservativebrief.com/"

    request = requests.get(urlOne,headers=headers)
    html = request.content

    soup = BeautifulSoup(html,'html.parser')

    news_list = []

    for h in soup.find_all("h2",{'class':"post-title"}):
        news_title = h.contents[0]
        if news_title not in news_list:
            news_list.append(news_title.text + " " + news_title.get('href'))




    for i, title in enumerate(news_list):
        print("Conservative Brief | ",i,':',title)


def dc_enq_scrapper():
    # Setting the URL you want to monitor
    urlOne = "https://dcenquirer.com/"

    request = requests.get(urlOne,headers=headers)
    html = request.content

    soup = BeautifulSoup(html,'html.parser')

    news_list = []

    for h in soup.find_all("h2",{'class':"front-view-title"}):
        news_title = h.contents[0]
        if news_title not in news_list:
            news_list.append(news_title.text + " " + news_title.get('href'))




    for i, title in enumerate(news_list):
        print("DC Enquirer | ",i,':',title)

con_brief_scrapper()
dc_enq_scrapper()