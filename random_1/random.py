# coding: utf-8
import random

from random_1.static_data import FOOD_LIST


def get_random_result():
    flag = 1
    restaurant = FOOD_LIST[random.randint(0, len(FOOD_LIST)-1)]
    result_restaurant_name = restaurant["restaurant_name"]
    food_list = restaurant["food_name"]
    if len(food_list):
        if len(food_list) == 1:
            result_food_name = food_list[0]
        else:
            result_food_name = food_list[random.randint(0, len(food_list)-1)]
    else:
        result_food_name = "该饭店还没有添加食物！"
        flag = 0
    result = {
        "restaurant": result_restaurant_name,
        "food": result_food_name,
        "flag": flag
    }

    return result


if __name__ == "__main__":
    result = get_random_result()
    while not result["flag"]:
        print("重来一次！")
        result = get_random_result()

    print("今天中午去[%s]吃[%s]。" %(result["restaurant"], result["food"]))