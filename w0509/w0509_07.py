import requests
from bs4 import BeautifulSoup

# html 파일을읽어와서 파일 html,css 형태로 파싱(변형)
with open("w0509/게시판2.html","r",encoding="utf8") as f:
    soup = BeautifulSoup(f,"lxml")
    
# data = soup.find("div",{"id":"input"})
# print(data.div.get_text())

# html 태그 찾는 방법 2개
# print(soup.thead)
# soup.find("thead",{"class":""})
data = soup.find("thead")
ths = data.find_all("th")
for th in ths:
    print(th.get_text())
