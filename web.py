#引入selenium库中的 webdriver 模块
from selenium import webdriver
import time

def search(content):
    
    #打开火狐浏览器
    driver = webdriver.Firefox()

    #打开百度搜索主页
    driver.get('https://www.baidu.com')
    driver.find_element_by_id("kw").send_keys(content)
    driver.find_element_by_id("su").click()
if __name__ == "__main__":
    search("从严治党从")
    key_word = "你好"
    url = "https://www.baidu.com/baidu?tn=monline_3_dg&ie=utf-8&wd="+key_word

