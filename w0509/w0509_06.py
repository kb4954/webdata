import requests

from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.naver"
headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

print(soup.title)
data = soup.find("div",{"class":"box_type_l"})
trs = data.tbody.find_all("tr")
trs2 = data.tbody.find_all("a")
# print(trs[1])
# print(trs[10])
print(trs2[0])
print(trs2[1])
print(trs2[2])
print(trs2[3])
print(trs2[4])


# print(len(trs))
# print(data.tbody.find_all("tr"))