from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
options = webdriver.ChromeOptions()
options.add_argument('--disable-infobars')  # 禁止策略化
options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
options.add_argument('window-size=1920x3000')  # 指定浏览器分辨率
options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug,这个是禁止GUU加速
options.add_argument('--incognito')  # 隐身模式（无痕模式）
options.add_argument('--disable-javascript')  # 禁用javascript
options.add_argument('--start-maximized')  # 最大化运行（全屏窗口）,不设置，取元素会报错
options.add_argument('--disable-infobars')  # 禁用浏览器正在被自动化程序控制的提示
options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
# options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
driver = webdriver.Chrome(options=options)
driver.get('https://www.junhun520.com/read/18012_12824144_2.html')
driver.minimize_window()
def shujv():
    s = WebDriverWait(driver, 5 ,0.001).until(
        EC.presence_of_element_located((By.CLASS_NAME,'content-ext'))
    ).text
    with open('xiaoshuo.txt','a',encoding='utf-8') as a:
        a.write(s)
    WebDriverWait(driver, 5, 0.001).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'btn-info'))
    ).click()
    # driver.find_elements_by_class_name('btn-info')[2].text
a = 1
for a in range(0,999):
    a+=1
    print('执行第%s次'%(a))
    shujv()
