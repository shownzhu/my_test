# coding: utf-8
import datetime

from crawler_2.main.test_try import test_try_1, test_try_2

if __name__ == "__main__":
    print("test_try_1开始执行！")
    print("开始执行1的时间：", datetime.datetime.now())
    test_try_1()
    print("结束执行1的时间：", datetime.datetime.now())
    print("test_try_1结束执行！")
    print("test_try_2开始执行！")
    print("开始执行2的时间：", datetime.datetime.now())
    test_try_2()
    print("结束执行2的时间：", datetime.datetime.now())
    print("test_try_2结束执行！")