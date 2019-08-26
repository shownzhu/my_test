# coding: utf-8


def test_try_1():
    n = 6000000
    myDict = {}
    for i in range(0, n):
        char = 'abcdefg'[i%6]
        if char not in myDict:
            myDict[char] = 0
        myDict[char] += 1
    print(myDict)


def test_try_2():
    n = 6000000
    myDict = {}
    for i in range(0, n):
        char = 'abcdefg'[i%6]
        try:
            myDict[char] += 1
        except KeyError:
            myDict[char] = 1
    print(myDict)