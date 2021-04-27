# coding: utf-8
import csv
from selenium import webdriver
import time

# from crawler_2.db.save_db import QQ_USER, QQ_PASSWORD


def get_qq_music_data(url, play_number):

    # 浏览器驱动程序
    executable_path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver"

    # 使用PhantomJS创建一个Selenium的Webdriver
    # driver = webdriver.Chrome(executable_path=executable_path)
    driver = webdriver.Edge()

    # # 使用PhantomJS创建一个Selenium的Webdriver
    # driver = webdriver.Chrome()

    # 创建一个csv文件
    csv_file = open('../date/data_yunda.csv', 'w', newline='', encoding='utf-8')
    writer = csv.writer(csv_file)
    writer.writerow(['跟踪记录'])
    # writer.writerow(['歌单标题', '作者', '播放数', '链接url', '作者主页url'])
    # index = 1

    driver.get(url)
    # time.sleep(10)

    data_str = driver.find_elements_by_class_name("content")[2].find_element_by_tag_name("table")

    th_list_str = data_str.find_elements_by_tag_name("th")
    th_list = list()
    for th in th_list_str:
        th_list.append(th.text)
    writer.writerow(th_list)

    tr_list = data_str.find_element_by_tag_name("tbody").find_elements_by_tag_name("tr")
    for tr in tr_list:
        td_list_str = tr.find_elements_by_tag_name("td")
        td_list = list()
        for td in td_list_str:
            td_list.append(td.text)
        writer.writerow(td_list)
    csv_file.close()
    print("抓取完成！")
    driver.quit()

    # qq登录
    # login_qq(driver, url)

    # 解析每一页歌单，直到第10页
    # while index < 11:
    #     print("第%s页正在抓取" % index)
    #
    #     data_list = load_page_get_data(driver, url, "playlist_box", "li")
    #
    #     # 解析歌单列表data_list
    #     for data in data_list:
    #         # 获取歌单的播放数(页面数据str)
    #         number_str = data.find_element_by_class_name("playlist__other").text
    #         # 先处理number_str, 拿到的str格式为：  播放量： 11万
    #         number_str = number_str[5:]
    #         # 获取播放数大于50万的歌单的封面
    #         if '万' in number_str and float(number_str.split("万")[0]) > play_number:
    #             number_int = int(float(number_str.split("万")[0]) * 10000)
    #             msk = data.find_element_by_css_selector("a.js_playlist")
    #             title_str = msk.get_attribute('title')
    #             href_str = msk.get_attribute('href')
    #             author = data.find_element_by_css_selector("a.js_user")
    #             author_name = author.get_attribute('title')
    #             author_page = author.get_attribute('href')
    #             writer.writerow([title_str, author_name, number_int, href_str, author_page])
    #
    #     print("第%s页抓取结束" % index)
    #     index += 1
    #     url = url[:-2] + str(index) + "&"
    #
    # csv_file.close()
    # print("抓取完成！")
    # driver.quit()


def load_page_get_data(driver, url, id, tag):
    flag_time = 1
    # 使用Webdriver加载页面
    driver.get(url)
    # # 切换到内容的iframe
    # driver.switch_to.frame("contentFrame")
    # 刷新页面--防止因js加载导致的元素id未改变
    driver.refresh()

    # 定位歌单标签--根据页面ID
    data_list = driver.find_element_by_id(id).find_elements_by_tag_name(tag)

    while flag_time < 11:
        if not data_list:
            print("flag_time:", flag_time)
            time.sleep(0.5)
            flag_time += 1
        else:
            break
        # 定位歌单标签--根据页面ID
        data_list = driver.find_element_by_id(id).find_elements_by_tag_name(tag)
    return data_list


# def login_qq(driver, url):
#     # qq音乐登录
#     first_page_url = url
#     driver.get(first_page_url)
#     login_element = driver.find_element_by_xpath("//a[@class='top_login__link js_login']")
#     login_element.click()
#     flag = True
#     i = 0
#     while flag:
#         try:
#             driver.switch_to.frame("frame_tips")
#             flag = False
#         except:
#             flag = True
#             time.sleep(1)
#             print("11111")
#     # 选择账号密码登录
#     password_element = driver.find_element_by_id("switcher_plogin")
#     password_element.click()
#
#     # 输入账号密码
#     u_element = driver.find_element_by_id("u")
#     p_element = driver.find_element_by_id("p")
#     u_element.send_keys(QQ_USER)
#     p_element.send_keys(QQ_PASSWORD)
#
#     # 取消自动登录勾选
#     select_element = driver.find_element_by_id("p_low_login_enable")
#     select_element.click()
#
#     # 点击登录
#     submit_element = driver.find_element_by_id("login_button")
#     submit_element.click()