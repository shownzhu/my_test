# coding: utf-8
import csv
from selenium import webdriver


def get_net_east_data_1():
    # 网易云音乐歌单的第一页url
    url = "https://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0"

    # 使用PhantomJS创建一个Selenium的Webdriver
    driver = webdriver.PhantomJS()

    # 创建一个csv文件
    csv_file = open('./date/playList.csv', 'w', newline='', encoding='utf-8')
    writer = csv.writer(csv_file)
    writer.writerow(['歌单标题', '播放数', '链接url'])
    index = 1

    # 解析每一页歌单，直到第10页
    while index < 11:
        print("第%s页正在抓取" % index)
        # 使用Webdriver加载页面
        driver.get(url)
        # 切换到内容的iframe
        driver.switch_to.frame("contentFrame")
        # 定位歌单标签--根据页面ID
        data_list = driver.find_element_by_id('m-pl-container').find_elements_by_tag_name("li")
        # 解析歌单列表data_list
        for data in data_list:
            # 获取歌单的播放数(页面数据str)
            number_str = data.find_element_by_class_name("nb").text
            # 获取播放数大于500万的歌单的封面
            if '万' in number_str and int(number_str.split("万")[0]) > 500:
                number_int = int(number_str.split("万")[0]) * 10000
                msk = data.find_element_by_css_selector("a.msk")
                title_str = msk.get_attribute('title')
                href_str = msk.get_attribute('href')
                writer.writerow([title_str, number_int, href_str])

        url = driver.find_element_by_class_name("znxt").get_attribute('href')
        print("第%s页抓取结束" % index)
        index += 1

    csv_file.close()
    print("抓取完成！")