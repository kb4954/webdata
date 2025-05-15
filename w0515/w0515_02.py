import requests

## 메일관련 import
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase 
from email import encoders
## 임시 비밀번호 발급하는것 html를 이메일로 보낼 예정
## password aaa1111로


## onulee@naver.com


#### 메일발송 ####
## 중요부분
recvMail = "onulee@naver.com" #받는사람 주소
password = "CGXQ1MCSDG58" ## 네이버 로그인 비밀번호를 입력해도 되지만, 파일이 노출

### 파일첨부 부분 ###
## MIME 객체화
msg = MIMEMultipart('alternative')
# 내용부분
text = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="ko" xml:lang="ko">
<head>
<meta http-equiv="Content-Type" content="application/xhtml+xml; charset=utf-8" />
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
<title> 비밀번호 발송 </title>


</head>
<body bgcolor="#FFFFFF" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" style="margin:0; padding:0; font:normal 12px/1.5 돋움;">


<table width="700" cellpadding="0" cellspacing="0" align="center">
<tr>
	<td style="width:700px;height:175px;padding:0;margin:0;vertical-align:top;font-size:0;line-height:0;">
		<img src="https://mail.naver.com/read/image/original/?mimeSN=1747272963.581223.166.30464&offset=1747&size=4808542&u=kb4954&cid=7c68d295d82db7b5fd7a7d518bb3ed7c@cweb008.nm&contentType=image/jpeg&filename=1747272941367.jpeg&org=1" />					
	</td>
</tr>
<tr>
	<td style="width:700px;height:78px;padding:0;margin:0;vertical-align:top;">
		<p style="width:620px;margin:50px 0 40px 38px;text-align:center;font-size:0;line-height:0;"><img src="https://mail.naver.com/read/image/original/?mimeSN=1747272963.581223.166.30464&offset=4810585&size=4805124&u=kb4954&cid=bb0ce3548a1833b9470efde67f38a2d@cweb012.nm&contentType=image/jpeg&filename=1747272957157.jpeg&org=1" alt="원두커피의 名家, JARDIN 임시 비밀번호가 발급되었습니다." /></p>
	</td>
</tr>
<tr>
	<td style="width:700px;height:196px;padding:0;margin:0;vertical-align:top;">
		<table width="618" height="194" cellpadding="0" cellspacing="0" align="center" style="margin:0 0 0 40px;border:1px #d9d9d9 solid;">
		<tr>
			<td style="width:618px;height:194px;padding:0;margin:0;vertical-align:top;font-size:0;line-height:0;background:#f9f9f9;">
				<p style="width:620px;margin:30px 0 0 0;padding:0;text-align:center;"><img src="https://mail.naver.com/read/image/original/?mimeSN=1747273017.193527.176.55040&offset=1899&size=4766834&u=kb4954&cid=58611112795af1d843928e016f577dd@cweb003.nm&contentType=image/jpeg&filename=1747272980841.jpeg&org=1" alt="JARDIN에서 비밀번호 찾기를 요청하셨습니다." /></p>
				<p style="width:620px;margin:10px 0 0 0;padding:0;text-align:center;color:#888888;font-size:12px;line-height:1;">아래의 PASSWORD는 임시 PASSWORD이므로 홈페이지 로그인 후 다시 수정해 주십시오.</p>
				<p style="width:620px;margin:28px 0 0 0;padding:0;text-align:center;color:#666666;font-size:12px;line-height:1;"><strong>임시 패스워드 : <span style="color:#f7703c;line-height:1;">aaa1111</span></strong></p>
				<p style="width:620px;margin:30px 0 0 0;padding:0;text-align:center;color:#888888;font-size:12px;line-height:1.4;">쟈뎅샵에서는 고객님께 보다 나은 서비스를 제공하기 위해 항상 노력하고 있습니다.<br/>앞으로 많은 관심 부탁드립니다.</p>
			</td>
		</tr>
		</table>	
	</td>
</tr>
<tr>
	<td style="width:700px;height:120px;padding:0;margin:0;vertical-align:top;">
		<p style="width:700px;margin:30px 0 50px 0;text-align:center;"><a href="#"><img src="https://mail.naver.com/read/image/original/?mimeSN=1747273017.193527.176.55040&offset=4769030&size=4769776&u=kb4954&cid=8ad55d42632a44382eb4588671fc91ea@cweb004.nm&contentType=image/jpeg&filename=1747272996671.jpeg&org=1" /></a></p>
	</td>
</tr>
<tr>
	<td style="width:700px;height:50px;padding:0;vertical-align:top;font-size:0;line-height:0;text-align:center;">
		<img src="https://mail.naver.com/read/image/original/?mimeSN=1747273017.193527.176.55040&offset=9539102&size=4757162&u=kb4954&cid=b118a88815c5d13186c61e65fc4a8e1@cweb002.nm&contentType=image/jpeg&filename=1747273005101.jpeg&org=1" alt="" />
	</td>
</tr>
<tr>
	<td style="width:700px;height:140px;padding:0;margin:0;vertical-align:top;background-color:#5a524c;">
		<p style="width:620px;margin:20px 0 0 40px;padding:0;text-align:center;line-height:1.5;color:#b2aeac;">메일수신을 원치 않으시는 분은 로그인 후. <span style="color:#ffffff">메일 수신 여부</span>를 변경해주시기 바랍니다.<br/>IF YOU DO NOT WISH TO RECEIVE EMAILS FROM US, PLEASE LOG-IN AND UPDATE<br/> YOUR MEMBERSHIP INFORMATION.</p>

		<p style="width:620px;margin:15px 0 0 40px;padding:0;text-align:center;line-height:1.5;color:#b2aeac;"><span style="color:#ffffff">본 메일에 관한 문의사항은 사이트 내 고객센터를 이용해주시기 바랍니다.</span><br/>COPYRIGHT ©  2014 JARDIN ALL RIGHTS RESERVED.</p>
	</td>
</tr>
</table>



</div>
</body>
</html>

"""
part2 = MIMEText(text,"html")
msg.attach(part2)
msg['From'] = "kb4954@naver.com"
msg['To'] = recvMail
msg['Subject'] = "임시비밀번호 발급"

## 메일발송부분   
s = smtplib.SMTP("smtp.naver.com",587)
s.starttls()
s.login("kb4954",password)
### 보내는 주소가 네이버메일이 아니면 에러처리 
# recvMails = 'kb4954@naver.com'
s.sendmail("kb4954@naver.com",recvMail,msg.as_string())
s.quit() 

print("메일발송 완료")


