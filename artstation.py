# -*- coding: utf-8 -*-
# author renmu
# blog www.irenmu.xyz

import os
import requests
from bs4 import BeautifulSoup
import math
import time
import re
from config import conf
from download import Download

print('''
版本：v2.0  
作者：仁暮
反馈地址：renmu12345678@gmail.com
不要信各种报毒！！再不信就就相信报毒软件吧╮(╯▽╰)╭我也没办法
''')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}

def get_work_pages(author):

    data_url = 'https://www.artstation.com/users/' + author + '/projects.json?page=1'
    # print(data_url)

    data_page = requests.get(data_url, headers=headers).json()

    total_count = data_page['total_count']  # 在第一个json文件中存在，为该作者的总作品数
    numbers = math.ceil(total_count / 50)  # json每次加载50个数据，总数/50向上取整，就是总的json数
    if numbers == 0:
        print('输入错误，请关闭程序重新输入')
        time.sleep(100)
    return numbers


def get_img_list(author, numbers, path):

    for number in range(1, numbers + 1):   # 50个为一个网址
        data_url = 'https://www.artstation.com/users/' + author + '/projects.json?page=' + str(number)
        data_page = requests.get(data_url, headers=headers).json()
        data = data_page['data']
        for i in range(len(data)):  # 循环一个网址
            permalink = data[i]['permalink']  # 图片地址

            page = requests.get(permalink, headers=headers)
            pattern = re.compile(r'image_url.*?\d{10}')  # 利用正则找出图片源地址
            items = re.findall(pattern, page.text)
            img_list = []
            for j in range(len(items)):  # 一套图有多张图
                img_url = items[j].replace(r'image_url\":\"', '')
                img_list.append({'pic_src': img_url, 'pic_id': img_url[-10:], 'pic_suffix': img_url[-15:-11]})

            download.thread_download(img_list, path)


if __name__ == '__main__':
    path = conf('day')  # 加载配置文件
    download = Download()
    author = input('''      
例如作者主页：https://www.artstation.com/artist/vins-mousseux    最后一个/后面就是要输入的内容
请输入作者id：''')
    numbers = get_work_pages(author)
    get_img_list(author, numbers, path)

    print(img_list)
