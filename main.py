# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: main.py
@time: 2020/10/13 11:37
@desc:
"""
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from crawldemo.spiders.baidu import BaiduSpider


def main():
    # 读取scrapy项目的配置文件
    settings = get_project_settings()
    # print(settings.copy_to_dict())
    # settings = {
    #     'DOWNLOAD_DELAY': 1.5
    # }
    # 创建一个CrawlerProcess对象
    process = CrawlerProcess(settings=settings)  # 括号中可以添加参数
    # process = CrawlerProcess()  # 括号中可以添加参数

    process.crawl(BaiduSpider)
    process.start()


if __name__ == '__main__':
    main()
