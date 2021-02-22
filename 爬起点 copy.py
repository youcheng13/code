import requests
from lxml import etree
import time
import sys		#以下三行是为了解决编码报错问题
# # reload(sys)
# sys.setdefaultencoding("utf8")

fo = open("xiaoshuo.txt","w")
i=1
for i in range(5):
    url = "https://m.78500.cn/kaijiang/p5/"
    header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
    r = requests.get(url,headers=header,time=)
    # 测试请求状态是否成功，返回200成功，返回300，400不成功
    print(r.status_code)

    data = r.text
    f = etree.HTML(data)

    hrefs = f.xpath('//*[@id="list"]/a//text()')
    print(hrefs)
    href = str()
    for href in hrefs:
        href = "https://m.78500.cn/"+href
        book = requests.get(href,headers=header).text
        e = etree.HTML(book)    
        title = e.xpath('/html/body/article/div[1]/h1/strong/text()')
        zuozhe = e.xpath('/html/body/article/div[2]/span/i//text()')
        # str = title+zuozhe
        # fo.write(str)
        for te in zuozhe:
            fo.write(te)
    print(href)

fo.close()
