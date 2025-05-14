import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

# 이메일 정보
sendMail = "kb4954@naver.com"
password = "CGXQ1MCSDG58"  # 네이버 '앱 비밀번호' 사용
recvMails = ['kb4954@naver.com', 'kkbb0221@gmail.com']

# MIME 객체 생성
msg = MIMEMultipart('alternative')
msg['From'] = sendMail
msg['To'] = ', '.join(recvMails)
msg['Subject'] = "시가총액 250개 주식정보를 보냅니다."

# 본문 내용
text = "이메일 글자 발송"
part2 = MIMEText(text, _charset='utf-8')
msg.attach(part2)

# 첨부파일 설정
file_path = "w0514/stock.csv"
if os.path.exists(file_path):
    part = MIMEBase('application', "octet-stream")
    with open(file_path, "rb") as f:
        part.set_payload(f.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment', filename='stock.csv')
    msg.attach(part)
else:
    print("⚠️ 첨부파일 경로가 잘못되었습니다:", file_path)

# 메일 발송
s = smtplib.SMTP("smtp.naver.com", 587)
s.starttls()
s.login(sendMail, password)

for recvMail in recvMails:
    s.sendmail(sendMail, recvMail, msg.as_string())

s.quit()
print("✅ 이메일 전송 완료")
