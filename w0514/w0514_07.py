import requests

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase # 문서화해서 파일을 보내는 명령어
from email import encoders

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
