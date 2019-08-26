# coding: utf-8
from crawler_2.main.get_music_163_data import get_net_east_data_1
from crawler_2.main.get_qq_music_data import get_qq_music_data
# from crawler_2.main.test import get_html_data_1

if __name__ == "__main__":
    print("crawler_2_main开始执行！")
    # 网易云音乐歌单的第一页url
    url = "https://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0"
    get_net_east_data_1(url, 500)
    # # qq音乐第一页
    # url = "https://y.qq.com/portal/playlist.html#t3=1&"
    # get_qq_music_data(url, 50)
    # url = "http://gecs.boeet.com.cn:81/res/svg/2cec81ea-0fa7-4d8c-b0f3-e53471af09f0.svg"
    # get_html_data_1(url)
    print("------------------------")
    print("crawler_2_main结束执行！")