# coding: utf-8
import csv
from selenium import webdriver


def get_html_data_1(url):

    # 使用PhantomJS创建一个Selenium的Webdriver
    driver = webdriver.Chrome()

    driver.get(url)

    html = driver.page_source

    print("抓取完成！")
    driver.quit()