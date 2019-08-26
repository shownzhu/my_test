import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup


# 打开url，获取html文件
def get_html_1():
    html = urlopen('http://jr.jd.com/')
    print(html.read())
    html.close()


# 标准工具
def get_html_2():
    # 网页下载
    html = urlopen('http://jr.jd.com/')
    html_str = html.read()
    print(html_str)
    # 网页解析
    bs_obj = BeautifulSoup(html_str, 'html.parser')
    # 获取a标签
    text_list = bs_obj.find_all('a', 'nav-item-primary')
    for text in text_list:
        print(text.get_text())
    html.close()


def get_time_test():
    start_time = datetime.datetime.now()
    print("start_time:", start_time)
    end_time = datetime.datetime.strptime("2018-09-06 10:20:00", '%Y-%m-%d %H:%M:%S')
    print("end_time: 2018-09-06 10:20:00")
    a = (start_time - end_time).seconds
    print("seconds:", a)
    print("hours:", a / 3600)