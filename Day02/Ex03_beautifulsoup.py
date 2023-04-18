'''

'''
import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/ranking/popularDay.naver'
headers = {'User-Agent' : 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
newsList = soup.find_all('a', class_='list_title')

print(len(newsList))

for news in newsList:
    print(news.text.strip())