import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase # 문서화해서 파일을 보내는 명령어
from email import encoders

# 중요부분
recvMail = "kb4954@naver.com" # 받는사람주소
password = "CGXQ1MCSDG58" 

# MIME 객체화
msg = MIMEMultipart('alternative')

# 내용부분
text = "이메일 글자 발송"
part2 = MIMEText(text, _charset='utf-8')
msg.attach(part2)
msg['From'] = "kb4954@naver.com"
msg['To'] = recvMail
msg['Subject'] = "시가총액 250개 주식정보를 보냅니다."

## 파일첨수
part = MIMEBase('application',"octet-stream")

## 파일읽어오기
with open("w0514/stock.csv","rb") as f:
    #part 담기
    part.set_payload(f.read())
    
# 파일첨부할 수 있는 형태로 인코딩
encoders.encode_base64(part) # 하나의 바이너리를 문자형태로 변환
# header 정보
part.add_header('Content-Disposition','attachment',filename='stock.csv')
msg.attach(part)

# 메일발송 부분
s =smtplib.SMTP("smtp.naver.com",587)
s.starttls()
s.login("kb4954@naver.com",password)
# 보내는 주소가 네이버 메일이 아니면 에러 처리
recvMails = ['kb4954@naver.com','kkbb0221@gmail.com']
for recvMail in recvMails:
    s.sendmail("kb4954@naver.com",recvMail,msg.as_string()) # 오른쪽은 받는사람
s.quit()
















