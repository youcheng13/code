#!/usr/bin/env python
#-*-coding:utf-8 -*-
import requests
from lxml import etree
# 需求：爬取海口58二手房的房源信息
if __name__ == "__main__":
    headers = {
        "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36"
    }
    # 抓取网页页面源码数据
    url = "https://haikou.58.com/ershoufang/?PGTID=0d100000-0080-50e7-1c6f-5d7ffc01b6ea&ClickID=4"
    r = requests.get(url=url,headers=headers)
    # 测试请求状态是否成功，返回200成功，返回300，400不成功
    # 可以写成:r = requests.get(url=url,headers=headers).text,为了可以打印状态码，所以就拆开写了
    print(r.status_code)
    r2 = r.text
    # 通过etree进行数据解析
    tree = etree.HTML(r2)
    # 通过xpath方法将标签对象存储到div_list列表中
    div_list = tree.xpath('//section[@class="list"]/div')
    # //*[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div[1]/a/div[2]/div[1]
    # //*[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div[1]/a/div[2]/div[2]
    # //*[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div[1]/a/div[2]/div[1]/section/div[1]/p[2]
    # 新建一个58.txt的文件，把下面循环得到的每个title保存进来
    fp = open('58.txt','w',encoding='utf-8')
    for div in div_list:
        # 局部解析div标签
        # 标题
        title = div.xpath('./a/div[2]/div[1]/div[1]/h3/text()')[0]
        # 价格
        title2 = div.xpath('./a/div[2]/div[2]/p/span[1]/text()')[0]
        # 平方数
        title3 = div.xpath('./a/div[2]/div[1]/section/div/p[2]/text()')[0]
        # 拼接成一条信息
        xinxi = title+"价格 = "+title2+"万"+title3+':'
        print(xinxi)
        # 把每一条拼接好的信息写入上面的fp中打开的58.txt
        fp.write(xinxi+'\n')

