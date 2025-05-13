import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import csv
import time

## fly1.html 불러오기
## 항공사, 출발시간, 도착시간, 금액

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# 브라우저 실행
broswer = webdriver.Chrome(options=options)

# 페이지 접속
url = "https://flight.naver.com/flights/domestic/GMP-CJU-20250607/CJU-GMP-20250608?adult=1&fareType=YC"
broswer.get(url)
time.sleep(3)  # 페이지 로딩 대기

with open("w0513/fly1.html","r",encoding="utf-8") as f:
    soup = BeautifulSoup(f,"lxml")
    
# 비행정보 모두 가져오기 
datas = soup.find_all("div",{"class":"domestic_Flight__8bR_b"})
print(len(datas)) # 287
datas_list = [] # list를 정렬할때 사용
for data in datas:
    # 항공사 이름
    airline = data.find("b",{"class":"airline_name__0Tw5w"}).get_text().strip()
    print(airline)
    # 출발시간
    times = data.find_all("b",{"class":"route_time__xWu7a"})
    startTime = times[0].get_text().strip()
    print(startTime)
    # 도착시간
    endTime = times[1].get_text().strip()
    print(endTime)
    # 가격
    price = data.find("i",{"class":"domestic_num__ShOub"}).get_text().strip().replace(",","")
    price = int(price)
    print(price)
    print('-'*50)
    
    datas_list.append([airline,startTime,endTime,price])

## list 정렬
# dd_list = sorted(datas_list,key=lambda x:x[3]) datas_list에 있는 [3]인 price로 순차정렬
dd_list = sorted(datas_list,key=lambda x:x[3], reverse=True) # 역순정렬
print(dd_list)





