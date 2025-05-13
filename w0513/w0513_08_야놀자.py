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

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# 브라우저 실행
browser = webdriver.Chrome(options=options)
browser.maximize_window()

# 야놀자 접속 
url = "https://nol.yanolja.com/"
browser.get(url)
time.sleep(2)
# 1. 호텔/리조트 클릭
elem = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div[2]/div/div[1]/a[1]/div/span[2]")
elem.click()
time.sleep(2)

# 2-1. 지역선택
elem = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[1]/div/div/button/span")
elem.click()
time.sleep(2)

# 2-2. 제주선택
elem = browser.find_element(By.XPATH,'//*[@id="_MODAL_DIM_"]/div/section/div[2]/div[1]/button[3]')
elem.click()
time.sleep(2)


# 2-3. 서귀포시/ 모슬포 선택
elem = browser.find_element(By.XPATH,'//*[@id="_MODAL_DIM_"]/div/section/div[2]/div[2]/div/div/button[2]')
elem.click()
time.sleep(2)

# 3. 6/7~6/8 적용하기 버튼 클릭
# 날짜 버튼 클릭
elem = browser.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/header/div[2]/div/button[1]/span/p').click()
time.sleep(2)
# 6/7 클릭
elem = browser.find_element(By.XPATH,'//*[@id="day-picker-2025-06"]/div[2]/div[1]/div[7]/button/span').click()
time.sleep(2)
# 6/8 클릭
elem = browser.find_element(By.XPATH,'//*[@id="day-picker-2025-06"]/div[2]/div[2]/div[1]/button/span').click()
time.sleep(2)
# 적용하기 버튼 클릭 
elem = browser.find_element(By.XPATH,'//*[@id="pc-dialog-sheet"]/div/div/div[3]/button').click()
time.sleep(2)

# 2. 지역선택 > 제주 > 서귀포시 / 모슬포 클릭
# 3. 6/7~6/8 적용하기 버튼 클릭
# 4. 스크롤 내리기
prev_height = browser.execute_script("return document.body.scrollHeight")

# 스크롤 내리기 반복 실행
while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height: break
    prev_height = curr_height
print("스크롤 내리기 종료")

# 5. 호텔,호텔이름,평점 없으면 없다라고 나오게끔, 후기개수 , 가격
## 먼저 가져오기 위해서 웹스크래핑을 해야됨
# soup = BeautifulSoup(browser.page_source,"lxml")
# with open("w0513/yanol.html","w",encoding="utf-8") as f:
#     f.write(soup.prettify())
    
# print("파일저장 완료")

# with open("w0513/yanol.html","r",encoding="utf-8") as f:
#     soup = BeautifulSoup(f,"lxml")

## 카테고리 호텔 모두 가져오기
# datas = soup.find_all("div",{"class":"flex w-full max-w-legacy-pc-size flex-wrap pc:rounded-12 divide-y divide-line-neutral-weak1 overflow-hidden border-b border-t border-line-neutral-weak1 pc:divide-x pc:border pc:first:!border-t pc:[&>*:nth-child(2)]:!border-t-0 pc:[&>*:nth-child(2n+1)]:!border-l-0"})
# for data in datas:
#     hotels = data.find("p",{"class":"text-text-neutral-sub typography-body-12-regular"})
#     print(hotels)







input("프로그램 종료 (엔터키)")