'''
pip install beautifulsoup4

url(uniform Resource Locator)
    인터넷에서 웹 페이지, 이미지, 동영상 등과 같은 리소스를 찾을 수 있는 주소

https://news.nate.com/rank/?mid=n1000

프로토콜(protocol)
    컴퓨터 네트워크를 통해 통신을 수행하기 위한 표준화된
    규칙, 절차, 혹은 통신 프로세스를 의미
    ex) 
        http/https - Hyper Text Trasfer Protocol 웹서버 접속
        ftp - 파일 서버 접속
        mailto - 메일서버 접속
        telnet - 원격지 접속

호스트(host)
    리소스가 위치한 서버의 이름
    ex) news.nate.com

포트(port)
    서버에서 사용하는 방번호
    ex)
    http - 80
    https - 443

경로(path)
    웹서버에서 리소스에 대한 경로(물리적 또는 추상적 경로)
    ex) /rank

쿼리(query) - 추가로 서버에 보내는 파라미터
    ex) mid=n1000
    key1=value1&key2=value2&key3=value3



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