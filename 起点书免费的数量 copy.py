
import requests
import os
from lxml import etree
if __name__ == "__main__":
    url = "https://www.qidian.com/search?kw=python&vip=0&page=1"
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:84.0) Gecko/20100101 Firefox/84.0"
	
        }
    r = requests.get(url=url,headers=headers)
    # 测试请求状态是否成功，返回200成功，返回300，400不成功
    # print(r.status_code)
    page_text = r.text
    tree = etree.HTML(page_text)
    zi = tree.xpath('//*[@id="result-list"]/div/ul/li[1]/div[1]/a/@href')[0]
    xin_url = "http:"+zi
    r2 = requests.get(url=xin_url,headers=headers)
    print(r2.status_code)
    p2 = r2.text
    tree2 = etree.HTML(p2)
    zi2 = tree2.xpath('/html/body/div/div[6]/div[1]/div[2]//text()')
    print(zi2)

    
    # for uurl in zi:
    #     uurl = uurl.xpath()
    #     print(uurl)
    #     r2 = requests.get(url=uurl,headers=headers)
    #     print(r.status_code)
        # print(zi)
        # print("起点排行免费书："+r2)
   
   

# //*[@id="result-list"]/div/ul/li//text()'