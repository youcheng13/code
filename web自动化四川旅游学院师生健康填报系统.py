
# 四川旅游学院师生健康填报系统
from helium import *
driver = start_chrome("http://health.sctu.edu.cn:56666/login.aspx")
un = "youcheng13@qq.com"
pw = "Chenggong999"
username = driver.find_element_by_id("TextBox1")
password = driver.find_element_by_id("TextBox2")
write(un,into=username)
write(pw,into=password)
enter = driver.find_element_by_id("Submit")
click(enter)


