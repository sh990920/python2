'''

'''
import requests
from bs4 import BeautifulSoup

url = 'https://music.bugs.co.kr/chart'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
musicList = soup.find_all('p', class_='title')
artistList = soup.find_all('p', class_='artist')

# for chart, artist in zip(musicList, artistList):
#     print(chart.text.strip(), end=' - ')
#     print(artist.text.strip())

for idx, chart in enumerate(musicList):
    print(chart.text.strip(), end=' - ')
    print(artistList[idx].find_all('a')[0].text.strip())