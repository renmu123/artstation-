# -*- coding:utf8 -*-

import configparser
import os

headers = {
    # "Host": "accounts.pixiv.net",
    # "Referer": "https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    # 'Origin': 'https://accounts.pixiv.net'
}
img_headers = {
    "Host": "i.pximg.net",
    "Referer": "https://www.pixiv.net",  # 图片服务器的headers referer是关键
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
}


def write_path(cf, args):
    if cf.has_option('path', args):
        path = cf.get('path', args)
    else:
        path = input('请输入保存地址：')
        path = comfirm_path(path)
        cf.set('path', args, path)
        cf.write(open('artstation.conf', 'w'))
    return path


# 配置文件
def conf(way):  # way是传递的参数，用来判断哪个函数调用了api
    cf = configparser.ConfigParser()
    cf.read('artstation.conf')
    if not cf.has_section('path'):  # 判断section 'path'是否存在
        cf.add_section('path')
        cf.write(open('artstation.conf', 'w'))
    return write_path(cf, way)


# 确认输入路径是否存在
def comfirm_path(path):
    if not os.path.exists(path):
        print('你输入的地址不存在，请重新输入')
        path = input('请输入保存地址：')
        comfirm_path(path)
    return path
