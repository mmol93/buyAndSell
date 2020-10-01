from selenium import webdriver
import time

browser = webdriver.Chrome("C:/selenium/chromedriver")

browser.get("https://www.mercari.com/jp/")  # 메루카리

def search_item():
    # 검색 부분에 아이템명 입력
    search_ele = browser.find_element_by_class_name("sc-kZmsYB celony").send_keys()

