# -*- coding: utf-8 -*-
import os
import config
# from src import login
from utlis import search
from utlis import newsread
from datetime import datetime
from utlis import downloadvideo

choice_dict = {
    "1": ["disaply_mode", newsread.read_news],
    "2": ["search", search.search_info],
    "3": ["download", downloadvideo.download_video]
}


# @login.login_in
def app():
    while True:
        for key, value in choice_dict.items():
            print("{} {}".format(key, value[0]))

        # 输入用户功能选择
        choice = input("please input your choice:").strip() # 去除不必要的空格
        if choice not in choice_dict.keys():
            print("it have not the choice, please input again")
            continue

        if choice.upper() == "Q":
            print("exit")
            break

        fun = choice_dict[choice][1]
        # 展示想要阅读的新闻条目
        if choice_dict[choice][0] == "disaply_mode":
            page_num = input("Enter the page number you want to see:").strip()

            # # 判断输入用户想看的页数
            # if not page_num.isdecimal():
            #     print("input error!")
            #     continue

            news_yeild = fun(page_num)
            next(news_yeild)

        elif choice_dict[choice][0] == "search":
            search_str = input("Enter the name you want to search:").strip()
            fun(search_str)
        else:
            search_str = input("Enter the name you want to search:").strip()

            if not search_str.isdecimal():
                print("input error!please input again")
                continue

            url = search.search_info(search_str)
            time_now = datetime.now()
            time_str = time_now.strftime("%Y-%m-%d-%H-%M-%S")
            file_path = os.path.join(config.USER_FILE_DIR, "视频{}{}.mp4".format(search_str, time_str))
            fun(url[0], file_path)


if __name__ == "__main__":
    app()
