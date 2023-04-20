'''
pip install selenium

selenium 패키지
    어플리케이션 테스트하기위한 프레임 워크 이다.
    웹 어플리케이션 다양한 브라우저 동작 테스트용
    웹 크롤링으로 많이 사용된다.
    java, python, c#, ruby 등 다양한 언어 지원
    ex) 브라우저 컨트롤로 사용

https://chromedriver.chromium.org/downloads

'''
import os
import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

import traceback

def download_images(keyword, num_images=10, output_dir='images'):
    #Chrome 드라이버 경로
    chrome_dirver_path = '/usr/local/bin/chromedirver'
    service = Service(executable_path=chrome_dirver_path)

    # Chrome 드라이버 인스턴스 생성
    driver = webdriver.Chrome(service=service)

    # Google 이미지 검색 페이지 접속
    driver.get('https://google.co.kr/imghp')

    # 검색어 입력 find_element
    search_bar = driver.find_element(By.NAME, 'q')
    search_bar.send_keys(keyword) # 키워드 입력
    search_bar.send_keys(Keys.RETURN) # 엔터 입력

    # 페이지 로딩 대기
    time.sleep(2)

    # 출력 디렉토리 생성
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 썸네일 요소 선택
    thumbnails = driver.find_elements(By.CSS_SELECTOR, ".rg_i")

    # 썸네일 클릭 및 이미지 다운로드
    for index, thumbnail in enumerate(thumbnails[:num_images]):
        try:
            thumbnail.click()
            time.sleep(2)

            # 이미지 요소 대기 및 선택
            image = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".r48jcc.pT0Scc.iPVvYb")
                )
            )
            # 이미지 URL 가져오기
            image_url = image.get_attribute("src")

            # 이미지 URL이 데이터 형식인 경우 건너뛰기
            if image_url.startswith("data:"):
                continue

            # HTTP 요청 헤더에 User_Agent 값을 추가하여 이미지 다운로드
            headers = {"User_Agent" : "Mozilla/5.0"}
            request = urllib.request.Request(image_url, headers=headers)
            with urllib.request.urlopen(request) as response:
                with open(f"{output_dir}/{keyword}_{index}.jpg", "wb") as out_file:
                    out_file.write(response.read())
    
        except Exception as e:
            print(f'Error downloadings image (index): {e}')
            traceback.print_exc()    

    # 드라이버 종료
    driver.quit()

# 실행 코드
keyword = 'cute cat'
num_images = 10
output_dir = 'images'

# 이미지 다운로드
download_images(keyword, num_images, output_dir)
