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

    # URLリストをロード
    urls_file = os.path.join(DATA_DIR, '_urls.txt')
    url_list = []
    with open(urls_file, 'r') as f:
        for i in f:
            url_list.append(i.rstrip('\n'))

    # Login
    bot = Bot(base_path=LOG_DIR)
    bot.login(username=username, password=password)

    # 画像をダウンロード
    for url in url_list:
        # get like medias from your timeline feed
        media_id = bot.get_media_id_from_link(url)
        # download
        dummy_file = os.path.join(DATA_DIR, str(media_id))
        bot.download_photo(
            media_id,
            filename=dummy_file
        )

if __name__ == '__main__':
    main()