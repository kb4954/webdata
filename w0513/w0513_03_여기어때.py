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

# 페이지 접ㅈ속
for j in range(1,6):
    url = f"https://www.yeogi.com/domestic-accommodations?keyword=%EA%B0%95%EB%A6%89&checkIn=2025-05-16&checkOut=2025-05-17&personal=2&freeForm=false&page={j}"
    browser.get(url)
    time.sleep(2) # 페이지 로딩 대기

    # print(browser.page_source) # 전체소스
    soup = BeautifulSoup(browser.page_source,"lxml")

    ### 위치점 가져오기
    data = soup.find("div",{"class":"css-1qumol3"})
    ### 1페이지 - 20개 정보 가져오기
    a_datas = data.find_all("a",{"target":"_blank"})
    ## 평점 9.1미만,평가수 1000미만 제외 후 출력

    for i,a_data in enumerate(a_datas):
        print(i+1) # 번호
        ## 제목
        title = a_data.find("h3",{"class":"gc-thumbnail-type-seller-card-title"})
        print(title.get_text())
        ## 평점 - 공백제거
        rank = a_data.find("span",{"class":"css-9ml4lz"})
        rank = float(rank.get_text().strip()) # 타입변경
        # 평가수 - 천단위 표시 제거
        rating = a_data.find("span",{"class":"css-oj6onp"}).strip().replace(",","")
        rating = int(rating[:-4])
        if rank <9.1 and rating <1000:
            print("***평점, 평가수 미만 제외 ***")
            continue
        else:print(rank,(rating[:-4])) ##[:-4]: "명 평가" 글자 제외
        ## 가격
        price = a_data.find("span",{"class":"css-5r5920"})
        try: ## 에러처리
            pass
        except:
            pass
        if price != None:## 중요 price가 없을때 get_text를 붙이면 에러가 남  
            print(price.get_text()) # 데이터가 없을때 출력시 error
        else:
            print("다른 날짜 확인")
        print("-"*30)
    


