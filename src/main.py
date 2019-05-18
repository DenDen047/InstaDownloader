import os
import sys
import re
import glob
import json
import random
import time

from instabot import Bot


PHOTO_DIR = "/photos"
VIDEO_DIR = "/videos"
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
    urls_file = os.path.join(PHOTO_DIR, '_urls.txt')
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
        # get media info
        info = bot.get_media_info(media_id)[0]
        # download
        dummy_file = str(media_id)
        if info['media_type'] == 1:     # photo
            bot.download_photo(
                media_id,
                filename=dummy_file,
                folder=PHOTO_DIR
            )
        elif info['media_type'] == 2:   # video
            bot.download_video(
                media_id,
                filename=dummy_file,
                folder=VIDEO_DIR
            )

if __name__ == '__main__':
    main()