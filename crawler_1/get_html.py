from urllib.request import urlopen
from bs4 import BeautifulSoup


# 打开url，获取html文件
def get_html_1():
    html = urlopen('http://jr.jd.com/')
    print(html.read())
    html.close()


def get_html_2():
    html = urlopen('http://jr.jd.com/')
    html_str = html.read()
    print(html_str)
    bs_obj = BeautifulSoup(html_str, 'html.parser')
    text_list = bs_obj.find_all('a', 'nav-item-primary')
    for text in text_list:
        print(text.get_text())
    html.close()