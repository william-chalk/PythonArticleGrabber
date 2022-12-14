from bs4 import BeautifulSoup
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials



scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]

#access the json key 
credentials = ServiceAccountCredentials.from_json_keyfile_name("python-article-script.json",scopes)

file = gspread.authorize(credentials) #Authenticates the JSON key with gspread

sheet = file.open("Article Database") #opens the google sheet

sheet1 = sheet.worksheet("Conservative Brief")
sheet2 = sheet.worksheet("DC Enquirer")





# Provider request header
headers = {'User-agent': 'Mozilla/5.0'}



def con_brief_scrapper():
    # Setting the URL you want to monitor
    urlOne = "https://conservativebrief.com/"

    request = requests.get(urlOne,headers=headers)
    html = request.content

    soup = BeautifulSoup(html,'html.parser')

    news_list = []

    count = 1

    for h in soup.find_all("h2",{'class':"post-title"}):
        news_title = h.contents[0]
        sheet1.update(f"A{count}",news_title.text)
        sheet1.update(f"B{count}",news_title.get("href"))
        count += 1
        print(count)
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

    count = 1

    for h in soup.find_all("h2",{'class':"front-view-title"}):
        news_title = h.contents[0]
        
        sheet2.update(f"A{count}",news_title.text)
        sheet2.update(f"B{count}",news_title.get("href"))
        count += 1
        if news_title not in news_list:
            news_list.append(news_title.text + " " + news_title.get('href'))




    for i, title in enumerate(news_list):
        print("DC Enquirer | ",i,':',title)

con_brief_scrapper()
dc_enq_scrapper()