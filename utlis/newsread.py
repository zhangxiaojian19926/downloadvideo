# -*- coding: utf-8 -*-
import config


# 获取文件行数--网上查找的方法，缓存指定大小的行数，并统计里面的换行符，从而计算出文件行数
def partial_count(file_name):
    """
    :param file_name: 输入文件名
    :return:
    """
    from functools import partial
    buffer = 1024 * 1024
    with open(file_name, mode="r", encoding="utf-8") as f:
        return sum(x.count('\n') for x in iter(partial(f.read, buffer), ''))


# 读新闻
def read_news(page_num, per_page_num=10):
    """
    :param page_num: 页码
    :param per_page_num:每一页展示的条数
    :return:
    """
    count = 0
    # 默认打印第一页
    if page_num == "":
        page_num = 1
    else:
        page_num = int(page_num)

    total_count = partial_count(config.USER_DATA_PATH)
    if total_count - page_num * per_page_num < 0 or per_page_num == 0:
        print("please input your page_num or per_page_num!")
        yield -1
    else:
        with open(config.USER_DATA_PATH, mode="r", encoding="utf-8") as video_config_object:
            # 跳过指定的的页数
            for i in range(page_num * per_page_num):
                video_config_object.readline()

            for item in video_config_object:
                print(item, end="")
                count = count + 1
                if count == 10:
                    count = 0
                    yield 1


# 主函数入口
if __name__ == "__main__":
    page_num = input("pages num:")
    per_page_num = input("per pages num:")
    v1 = read_news(int(page_num), int(per_page_num))
    print(v1)
    if v1 == -1:
        pass
    else:
        next(v1)
