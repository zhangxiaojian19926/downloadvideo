# -*- coding: utf-8 -*-
import os
import sys

# 配置对应的用户目录
USER_FILE = os.path.dirname(os.path.abspath(__file__))
USER_DB_PATH = os.path.join(USER_FILE, "db", "user.txt")
USER_FILE_DIR = os.path.join(USER_FILE, "files")  # 路径拼接，不会去创建指定文件
USER_DATA_PATH = os.path.join(USER_FILE, "db", "video.csv")

# 添加当前工程路径到系统查找目录，防止工程路径未被添加到第三方模块路径中
sys.path.append(USER_FILE)