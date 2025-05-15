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

## 메일관련 import
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase 
from email import encoders


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

### csv 파일 만들기
f = open('w0515/news.csv','w',encoding='utf-8-sig',newline='') # 빈공백을 하나 넣어줘야 엔터키가 두번 안들어감.
writer = csv.writer(f)

title = ['언론사','기사제목']
writer.writerow(title) # csv 리스트 저장 


### 1. 네이버 접속
url = "https://news.naver.com/main/ranking/popularDay.naver"

browser.get(url)

## html 파싱
soup = BeautifulSoup(browser.page_source,"lxml")
## 언론사별 랭킹 뉴스 전체
data = soup.find("div",{"class":"rankingnews_box_wrap"})
## 12개의 랭킹박스 찾기
rNews = data.find_all("div", {"class":"rankingnews_box"})
## 랭킹박스를 for문으로 돌려서 반복문 만들기


## 12번 반복해서 가져옴
for r in rNews:
    # test용으로 먼저 for문 밖에서 테스트 하기신문사 이름 가져오기
    newsName = r.find("strong",{"class":"rankingnews_name"}).get_text().strip()
    print(newsName)

    ## 기사제목 가져오기
    newsContent = r.find("a",{"class":"list_title"}).get_text().strip()
    print(newsContent)
    
    writer.writerow([newsName,newsContent]) # 그냥 리스트로 넣으면 됨.

# 파일 생성 완료
f.close()
## 파일 생성동안 잠시 대기
time.sleep(2)


# news.csv파일로 만들어서 
# 신문사 기사
# 뉴시스,'전원일기 일용이' 박은수 수천만원 사기혐의로 피소
# 한국경제

# 파일첨부 메일로 발송
# 제목 : 네이버 랭킹뉴스 보냄.
# 내용 : 네이버 12개 랭킹 1위 뉴스를 보내드립니다.
# 보내는 주소 : onulee@naver.com


## 중요부분
recvMail = "kb4954@naver.com" #받는사람 주소
password = "CGXQ1MCSDG58" ## 네이버 로그인 비밀번호를 입력해도 되지만, 파일이 노출


### 파일첨부 부분 ###
## MIME 객체화
msg = MIMEMultipart('alternative')
# 내용부분
text = """<h2>랭킹뉴스 기사 모음<h2>
<img src='https://mail.naver.com/read/image/original/?mimeSN=1747271378.145475.162.30464&offset=1721&size=4808542&u=kb4954&cid=067c45997358b5e40495e612b0f41f@cweb001.nm&contentType=image/jpeg&filename=1747271369984.jpeg&org=1'>
""" ## 여기에 소스를 넣으면 소스통채로 메일로 보낼 수 있음(풀주소로 나 보내야함)

part2 = MIMEText(text,"html")
msg.attach(part2)
msg['From'] = "kb4954@naver.com"
msg['To'] = recvMail
msg['Subject'] = "언론사별 랭킹뉴스를 보냅니다."

## 파일첨부
part = MIMEBase('application',"octet-stream")
## 파일읽어오기
with open('w0515/news.csv',"rb") as f:
    #part담기
    part.set_payload(f.read())

#파일첨부할수 있는 형태로 인코딩
encoders.encode_base64(part) 
## header 정보
part.add_header('Content-Disposition','attachment',filename='news.csv')
msg.attach(part)

## 메일발송부분   
s = smtplib.SMTP("smtp.naver.com",587)
s.starttls()
s.login("onulee",password)
### 보내는 주소가 네이버메일이 아니면 에러처리 
# recvMails = ['onlee@naver.com','onulee74@gmail.com']
# for recvMail in recvMails:
s.sendmail("kb4954@naver.com",recvMail,msg.as_string())
s.quit() 

print("메일발송 완료")


input("프로그램 종료시 엔터")
