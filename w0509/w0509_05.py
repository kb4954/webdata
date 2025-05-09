import requests
from bs4 import BeautifulSoup

# url = ""
# headers = ""
# res = requests(url,headers=headers)
# soup = BeautifulSoup(res.text,"lxml")
with open("w0509/a.html","r",encoding="utf8") as f:
    soup = BeautifulSoup(f,"lxml")
# soup = BeautifulSoup("w0509/a.html","lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.h2)
# print(soup.find_all("h2"))
# print(soup.find("p",{"id":"p1"}).get_text())
# print(soup.find("ul"))
# print(soup.find("div",{"class":"c2"}).find("ul").find("li")) ## 두번째꺼 맨처음 li를 가져옴
print(soup.find("div",{"class":"c1"}).find("ul").find_all("li")[1].get_text())
print(soup.find("ul").find_all("li")[1].get_text())## 위에랑 같음

print(soup.find("div",{"class":"c2"}).find("ul").find_all("li")[0].get_text())
print(soup.find("div",{"class":"c2"}).find("ul").find_all("li")[2].get_text())

datas = soup.find("ul").find_all("li")
for data in datas:
    print(datas.get_text())