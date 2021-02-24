from selenium import webdriver
import time
wd = webdriver.Chrome("/Users/yc/chromedriver")#如果路径有设置好就不需要再这里指定了
# 对服务器放回的响应等待10秒，不然有是服务器还没有返回数据，而本地的浏览器驱动已经返回给了python没有数据，就会出现报错
wd.implicitly_wait(10)
wd.get("http://www.baidu.com")
wd.find_element_by_id("kw").send_keys('美女\n')
# wd.find_element_by_id('su').click(),上面的美女后面加了回车，所以就不用再点击了
# time.sleep(3),上面第四行wait解决了
time.sleep(3)
wd.find_element_by_xpath('//*[@id="s_tab"]/div/a[3]').click()
# 关闭浏览器和启动
wd.quit()

# for tu in tupian:
#     tu_url = tu.find_element_by_xpath('./@data-thumburl')
#     print(tu_url)
# wd.find_elements_by_id("su")
# wd.click()

# wd.find_element_by_xpath('//*[@id="kw"]').send_keys('python')
# wd.find_element_by_xpath('//*[@id="su"]').click()



