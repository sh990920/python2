'''
pip install beautifulsoup4
'''
import requests
from bs4 import BeautifulSoup
# https://news.nate.com/rank/?mid=n1000
url = 'https://news.nate.com/rank/'
param = { "mid" : "n1000" }
response = requests.get(url, params=param)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
#titList = soup.find_all('div', class_='mlt01')
titList = soup.find_all('strong', class_='tit')
for tit in titList:
    print(tit.text.strip())
    # print(tit.find('strong', class_='tit').text.strip())