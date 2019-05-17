import os
import sys
import re
import glob
import json
import random
import time

from instabot import Bot


DATA_DIR = "/data"
LOG_DIR = "/log"
CONFIG_DIR = "/configs"

# 初期設定
random.seed(time.time())


def main():
    # アカウント情報をロード
    with open('account_info.json', 'r') as f:
        data = json.load(f)
        username = data['username']
        password = data['password']

    # Login
    bot = Bot(
        base_path=LOG_DIR,
        comments_file=os.path.join(CONFIG_DIR, 'comments.txt')
    )
    bot.login(username=username, password=password)

    # 画像をダウンロード
    dummy_file = os.path.join(DATA_DIR, str(media_id))
    bot.download_photo(
        media_id,
        filename=dummy_file
    )

if __name__ == '__main__':
    main()