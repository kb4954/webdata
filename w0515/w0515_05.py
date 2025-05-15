## 네이버 항공권
# 김포, 제주 5/31 6/1 ->
# 금액 90000원 이하는 제외
# 출발 시간 17:00 이상은 제외 

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
import pyautogui # 마우스 제어

from datetime import datetime
standard_time = datetime(2025,5,31,17,00,00)
now_time = datetime(2025,5,31,15,00,00)

print(standard_time)
print(now_time)
print(standard_time > now_time)







# 크롬 옵션 설정 - 셀레니움 접근 제한 : 보안
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# 브라우저 실행
browser = webdriver.Chrome(options=options) 
browser.maximize_window() # 창 최대화




# 1. 네이버 항공권 접속
url = "https://flight.naver.com/flights/domestic/SEL-CJU-20250531/CJU-SEL-20250604?adult=1&fareType=YC"
browser.get(url)
time.sleep(2)
pre_height = browser.execute_script("return articleListArea.scrollHeight")
print("처음화면 높이 : ",pre_height)
















# 자바스크립트의 스크롤 내리기를 사용해서 진행
# browser.execute_script("window.scroll(0,articleListArea.scollHeight)")
pyautogui.moveTo(50,700)
time.sleep(2)
while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    # 변화된 현재 높이
    curr_height = browser.execute_script("return document.body.scrollHeight")
    print("변화된 현재 높이: ",curr_height)
    # 높이의 변동이 없으면 멈추면 됨.
    if curr_height == pre_height:
        break
    pre_height = curr_height



soup = BeautifulSoup(browser.page_source,"lxml")

## 항공권 박스

## 항공권 리스트 가져오기
airlines =  soup.find_all("div",{"class":"domestic_Flight__8bR_b"})

### 12만원 이하
for airline in airlines:
    price = airline.find("div",{"class":"domestic_item__5CAye"}).get_text().strip()
    p_line = price.split("원")  # '10억 9,000 -> ['10','9000']
    price_line = int(p_line[0])
    
    # 12만원 초과는 제외
    if price_line > 120000 : continue
    print(price_line)
    # 상단타이틀
    title = data.find("div",{"class":"item_domestic_select_schedule__IR7_Ntitle"}).get_text().strip()
    print(title)
    # 출발시간
    start_time = data.find("span",{"class":"route_time__xWu7a"}).get_text().strip()
    print(start_time)
    # 출발시간 17:00 이후는 제외
    s_time = start_time.replace(":","")
    if s_time > 1700: continue
    print(s_time)
    print("-"*30)

input("프로그램 종료 엔터")




# # import datetime
# from datetime import datetime

# # 기준 시간
# standard_time = datetime(2025,5,31,17,00,00)
# # 검색된 시간 - "06:15"
# times = "06:15"
# d_time = times.split(":") 
# search_time = datetime(2025,5,31,int(d_time[0]),int(d_time[1]),00)

# if(standard_time < search_time): # 기준시간보다 검색된 시간이 더 크면 제외
#     print("제외 대상입니다.")
# else:
#     print("데이터 출력")