# -*- coding: utf-8 -*-
import re
import config


def search_info(search_str):
    """
    :param search_str: 待查找的字符串
    :return:
    """
    with open(config.USER_DATA_PATH, mode="r", encoding="utf-8") as video_name_object:
        for item in video_name_object:
            if search_str == "":
                break
            if search_str.isdecimal() and item.split(",")[0] == search_str:
                download_https = re.findall("[a-za-z]+://[^\s]*", item) #匹配当前字符串中的网页地址
                print(item, end = "")
                return download_https
            elif re.findall("{}".format(search_str), item) != []:
                print(item, end="")


if __name__ == "__main__":
    search_str = input("please input your string:")
    search(search_str)
