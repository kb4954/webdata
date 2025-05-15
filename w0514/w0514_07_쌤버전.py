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
url = "https://news.naver.com/main/ranking/popularDay.naver"
# news.csv파일로 만들어서 
# 신문사 기사
# 뉴시스,'전원일기 일용이' 박은수 수천만원 사기혐의로 피소
# 한국경제

# 파일첨부 메일로 발송
# 제목 : 네이버 랭킹뉴스 보냄.
# 내용 : 네이버 12개 랭킹 1위 뉴스를 보내드립니다.
# 보내는 주소 : onulee@naver.com

# 중요부분
recvEmail = "kb4954@naver.com"
password = "CGXQ1MCSDG58" 

# MIME 객체 생성
msg = MIMEMultipart()
msg['From'] = "kb4954@naver.com"
msg['To'] = recvEmail
msg['Subject'] = "네이버 랭킹뉴스 보냄"

# 본문내용 
text = "네이버 12개 랭킹 1위 뉴스를 보내드립니다."
part2 = MIMEText(text, _charset='utf-8')
msg.attach(part2)

# 파일 읽어오기
part = MIMEBase('application',"octet-stream")
with open("w0514/new.csv","rb") as f:
    part.set_payload(f.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition','attachment',filename='news.csv')
msg.attach(part)


# 메일 발송 부분
s =smtplib.SMTP("smtp.naver.com",587)
s.starttls()
s.login("kb4954@naver.com",password)
# 보내는 주소가 네이버 메일이 아니면 에러 처리
s.sendmail("kb4954@naver.com",recvEmail,msg.as_string()) # 오른쪽은 받는사람
s.close()
print("메일 발송 완료")
