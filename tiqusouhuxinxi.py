import requests
from bs4 import BeautifulSoup
import re
r = requests.get("https://sports.sohu.com")
print(r.status_code)#如果成功返回200，不成功返回300，400等
html = r.text
soup = BeautifulSoup(html,"html.parser")#通过"html.parser"解析器进行解析
xws= soup.find_all("div",class_="s-one_center")#通过find_all进行全部数据提取
for xw in xws:
	print(xw.get_text())#提取之后输出到xw.text
