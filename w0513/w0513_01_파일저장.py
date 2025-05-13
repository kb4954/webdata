import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import csv
import time

# 크롬 옵션 설정 - 셀레니움 접근 제한 : 보안
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)


# 브라우저 실행
browser = webdriver.Chrome(options=options) 

# 웹접근 두가지 방법 requests 와 selenium 
## requests는 자바나 ajax react에서 만들어진 동적 웹페이지를 가져올수없음
## selenium은 가능 대신 좀 느림 두가지다 웹 추출 ->  BeautifulSoup


# 페이지 접속
url = "https://edu1032.shiningcorp.com/index.php?device=pc&designkits=1"
browser.get(url)
time.sleep(2) # 페이지 로딩 대기

# print(browser.page_source)
soup = BeautifulSoup(browser.page_source,"lxml")

# 파일저장
with open("w0513/temple1.html","w",encoding="utf-8") as f:
    f.write(soup.prettify())

# 프로그램 종료
input("프로그램 종료(엔터키 입력)")




