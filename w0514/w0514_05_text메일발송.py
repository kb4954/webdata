import smtplib
from email.mime.text import MIMEText

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

# 중요정보
smtpName = "smtp.naver.com"
smtpPort = 587

sendEmail = "kb4954"
password = "CGXQ1MCSDG58" ## 네이버 로그인 비밀번호를 입력해도 되지만,파일이 노출 

recvEmail = "kb4954@naver.com"

title = "웹스크래핑 이메일 보내기"
text = "날씨정보 오늘 날씨: 맑음, 내일 날씨: 흐리고 비"

msg = MIMEText(text)
msg['Subject'] = "웹스크래핑 이메일 보내기"
# 네이버 주소 메일이 아니면 에러
msg['From'] = "kb4954@naver.com"
msg['To'] = recvEmail

s =smtplib.SMTP("smtp.naver.com",587)
s.starttls()
s.login("kb4954@naver.com",password)
# 보내는 주소가 네이버 메일이 아니면 에러 처리
s.sendmail("kb4954@naver.com",recvEmail,msg.as_string()) # 오른쪽은 받는사람
s.close()

print("메일 발송 완료")




