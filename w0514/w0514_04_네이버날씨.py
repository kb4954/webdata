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

# 크롬 옵션 설정 - 셀레니움 접근 제한 : 보안접근 해제 안하면 여러번 쌓일 경우 차단될 수 있음.
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# # 브라우저 실행
browser = webdriver.Chrome(options=options) # 크롬 드라이버 없으면 위치점 지정해야함.
browser.maximize_window() # 창 최대화

# 네이버 접속
# url = "https://www.naver.com/"
# browser.get(url)
# time.sleep(2)

# selenium
# 1. 네이버 접속
# 2. 뉴스클릭 - 탭 2번째
# 3. 총 12개의 뉴스를 출력하시오 . 상단첫번째것만 출력하시오

# 뉴스클릭
# url = "https://news.naver.com/"
# browser.get(url)
# elem = browser.find_element(By.XPATH,'//*[@id="shortcutArea"]/ul/li[5]/a/span[2]').click()
# time.sleep(2)
url = "https://weather.naver.com/r"
browser.get(url)
time.sleep(1)
soup = BeautifulSoup(browser.page_source,"lxml")
data = soup.find("ul",{"class":"box_color"})
lis = data.find_all("li")
txt  = ""
for li in lis:
    date = li.find("span",{"class":"date"})
    print(date.get_text().strip())
    Weathers = data.find_all("apan",{"class":"weather_inner"})
    for w in Weathers:
        am = w.find("span",{"class":"timeslot"}).get_text()
        print(am,end=",")
        txt += am +":"
        tWeather = w.find("span",{"class":"weather_text"}).get_text().strip() # 맑음 맑음
        print(tWeather)
    
    # print(tWeather)
    






# 웹스크래핑 시작 
# 현재기온 출력 
# tTemp = soup.find("strong",{"class":"card_now_temperature"}).get_text()
# print("현재온도 : ",tTemp)

# # 현재 날씨 출력
# tWeather = soup.find("em",{"class":"card_date_emphasis"}).get_text()
# print("현재날씨 : ",tWeather)

# 최저온도
tLow = soup.find("dd",{"class":"card_description_data"}).get_text()
print("최저온도 : ",tLow)

# 최고온도
tHigh = soup.find("dd",{"class":"card_description_data"}).get_text()
print("최저온도 : ",tHigh)




# 내일 최저온도
# 내일 최고온도
# 내일 오전 날씨
# 내일 오후 날씨





# 뉴스 내용출력 
# newssct = soup.find("article",{"id":"dic_area"})
# print(newssct.get_text())
# time.sleep(1)
# browser.back()


## 랭킹뉴스 들어가서 뉴스 클릭 
## 첫번째 뉴스 클릭 




## 프로그램 종료
input("프로그램 종료시 엔터")




 