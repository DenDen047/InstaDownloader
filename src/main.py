import os
import sys
import re
import glob
import json
import random
import time
import datetime

from instabot import Bot


ROOT_DATA_DIR = "/root_data"
PHOTO_DIR = "/root_data/photos/{}".format(datetime.date.today().strftime("%Y-%m-%d"))
VIDEO_DIR = "/root_data/videos/{}".format(datetime.date.today().strftime("%Y-%m-%d"))
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

    # create directories
    dirs = [PHOTO_DIR, VIDEO_DIR]
    for d in dirs:
        if not os.path.exists(d):
            os.makedirs(d)

    # URLリストをロード
    urls_file = os.path.join(ROOT_DATA_DIR, '_urls.txt')
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

    # delete directories which have no data
    dirs = [PHOTO_DIR, VIDEO_DIR]
    for d in dirs:
        if not os.listdir(d):
            os.rmdir(d)

if __name__ == '__main__':
    main()