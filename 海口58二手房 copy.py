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
    # fp = open('58.xlsx','w',encoding='utf-8')

#     file = xlwt.Workbook()

# table = file.add_sheet('sheet1', cell_overwrite_ok = True)

# table.write()
    zong = []
    for div in div_list:
        # 局部解析div标签
        title = div.xpath('./a/div[2]/div[1]/div[1]/h3 |./a/div[2]/div[2]/p/span[1] | ./a/div[2]/div[1]/section/div/p[2]')
        
        for zong in title:
            xinxi = zong.xpath('./text()')[0] 
            zong.append(xinxi)

        # print(xinxi)
        # fp.write(xinxi+'\n')

        # 解决乱码的问题
        # 1.在接收到response数据的时候，把它手动编码成"utf-8",因为Python默认就是"utf-8"格式
        # response.encoding = "utf-8"
        # 2.对某个文字进行编码
        # name.encode("iso-8859-1").decode("gbk")

