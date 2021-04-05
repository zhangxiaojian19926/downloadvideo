# -*- coding: utf-8 -*-
import requests
import functools
import time


def outer(origin):
    @functools.wraps(origin)
    def inner(url, file_name):
        print("正在下载中...")
        start = time.time()
        origin(url, file_name)
        end = time.time()
        print("\n全部下载完成！用时{:.2f}".format(float(end - start)))

    return inner


@outer
def download_video(url=None, file_name=None):
    """
    :param url: 输入待下载的url
    :param file_name: 文件保存目录
    :return:
    """
    # 获取指定网站的内容
    res = requests.get(
        url=url,
        headers={
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 FS"
        }
    )

    # 视频总大小（字节）
    file_size = int(res.headers['Content-Length'])
    print("[文件大小]:{:.2f}M".format(file_size / 1024 / 1024))

    download_size = 0
    with open(file_name, mode='wb') as file_object:
        # 分块读取下载的视频文件（最多一次读128字节），并逐一写入到文件中。 len(chunk)表示实际读取到每块的视频文件大小。
        for chunk in res.iter_content(1024):
            download_size += len(chunk)
            file_object.write(chunk)
            file_object.flush()
            # message = "视频总大小为：{}字节，已下载{}字节。".format(file_size, download_size)
            # print(message)
            print("\r已下载{:.2f}%".format(float(download_size / file_size * 100)), end="")
        file_object.close()
    res.close()


if __name__ == "__main__":
    pass
