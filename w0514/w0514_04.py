import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
import random
# 크롬 옵션 설정 - 셀레니움 접근 제한 : 보안접근 해제
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
# 브라우저 실행
browser = webdriver.Chrome(options=options)
browser.maximize_window() # 창 최대화
### 1. 네이버 접속
# url = "https://www.naver.com/"
url = "https://news.naver.com/main/ranking/popularDay.naver"
browser.get(url)
def newsSearch(nXpath):
    time.sleep(1)
    # 뉴스부분 클릭
    browser.find_element(By.XPATH,nXpath).click()
    # 웹스크래핑시작
    soup = BeautifulSoup(browser.page_source,"lxml")
    data = soup.find("div",{"class":"media_end_head_title"})
    # 뉴스제목출력
    title = data.find("span").get_text()
    print(title)
    # 뉴스내용출력
    newssct = soup.find("article",{"id":"dic_area"})
    print(newssct.get_text())
    time.sleep(1)
    # 뒤로 가기
    browser.back()
    
    
    with open("w0514/new.csv","w",encoding="utf-8") as f:
        f.write(soup.prettify()) # html 파일 저장
for i in range(1,13):
    ## 1. 뉴스 클릭
    nXpath = f'//*[@id="wrap"]/div[4]/div[2]/div/div[{i}]/ul/li[1]/div/a'
    newsSearch(nXpath)


## 랭킹뉴스 들어가서 뉴스 클릭 
## 첫번째 뉴스 클릭 




## 프로그램 종료
input("프로그램 종료시 엔터")




 