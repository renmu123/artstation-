# -*- coding:utf8 -*-
import os
import time
import threading

import requests
from bs4 import BeautifulSoup
from config import headers



class Download:

    def download_for_view(self, pic_src, pic_id, pic_suffix, path):
        # print(path)
        try:
            os.mkdir(path)
        except:
            pass
        extension = pic_suffix  # 扩展名
        name = pic_id + extension
        name_path = os.path.join(path, name)
        print(name_path)
        # print(pic_src)
        try:
            img = requests.get(pic_src, headers=headers)
        except:
            time.sleep(3)
            img = requests.get(pic_src, headers=headers)
        with open(os.path.join(path, name), 'ab') as f:
            f.write(img.content)


    # 下载图片
    # def download(self, pic_src, pic_id, pic_suffix, path):
    #     if os.path.isfile(os.path.join(path, pic_id + pic_suffix)):  # 如果文件存在
    #         return True
    #     else:
    #         self.download_for_view(pic_src, pic_id, pic_suffix, path)
    #     if os.path.exists(os.path.join(path, pic_id)):  # 判断文件夹存在
    #         self.download_for_view(pic_src, pic_id, pic_suffix, os.path.join(path, pic_id))
    #     else:
    #         path_name = os.path.join(path, pic_id)
    #         os.makedirs(path_name)
    #         self.download_for_view(pic_src, pic_id, page_count, path_name)

    # 多线程下载
    def thread_download(self, img_list, path):
        threads = []
        for url in img_list:
            pic_src = url.get('pic_src')
            pic_id = str(url.get('pic_id'))
            pic_suffix = url.get('pic_suffix')
            t = threading.Thread(target=self.download_for_view, args=[pic_src, pic_id, pic_suffix, path])
            threads.append(t)

        for t in threads:
            t.start()
            while True:
                # 判断正在运行的线程数量,如果小于5则退出while循环,
                # 进入for循环启动新的进程.否则就一直在while循环进入死循环
                if (threading.active_count() < 10):
                    break
        for t in threads:
            t.join()
        # print('下载完成')

