# coding = utf-8

from bs4 import BeautifulSoup

from selenium import webdriver

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import os

import sys

import socket

import time

dcap = dict(DesiredCapabilities.PHANTOMJS)

dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393")

js2 = 'window.scrollTo(0, document.body.scrollHeight)'

reload(sys)
sys.setdefaultencoding( "utf-8" )


class crawl_wechat:

    def __init__(self, url):

        self.url = url

        self.old_scroll_height = 0

    def getList(self):

        driver = webdriver.PhantomJS(desired_capabilities=dcap)

        driver.get(self.url)
        for j in range (10):
            for i in range(1000):
                driver.execute_script(js2)
            time.sleep(30)

        print "loading completed\n"

        resp = BeautifulSoup(driver.page_source, 'html5lib')
        msg_list = []

        msg_cover = resp.find_all("div", class_="msg_cover")

        for href in msg_cover:
            if href.get("hrefs") is not None:
                msg_list.append(href.get("hrefs"))
            else:
                msg_cover_redirect = resp.find_all("a",class_="cover_appmsg_link_box redirect")
                for tmp in msg_cover_redirect:
                    msg_list.append(tmp.get("hrefs"))

        sub_msg = resp.find_all("h4", class_="weui_media_title")

        for sub_href in sub_msg:
            msg_list.append(sub_href.get("hrefs"))

        list_lenth = len(msg_list)
        count_time = 0
        #print msg_list
        fh = open("35.txt",'w')
        while(count_time < list_lenth):
            urls = msg_list[count_time]
            fh.write(urls)
            fh.write('\n')
            count_time = count_time + 1
        fh.close()

if __name__ == '__main__':

    wechat_url = sys.argv[1]

    wechat = crawl_wechat(wechat_url)

    wechat.getList()
