
# 四川旅游学院师生健康填报系统
from helium import *
driver = start_chrome("https://mail.qq.com/")
un = "youcheng13@qq.com"
pw = "Chenggong999"
username = driver.find_element_by_css_selector("#uinArea label[style=display: none")
password = driver.find_element_by_class_name("inputstyle password")
write(un,into=username)
time.sleep(10)
write(pw,into=password)
time.sleep(10)
enter = driver.find_element_by_id("login_button")
click(enter)


