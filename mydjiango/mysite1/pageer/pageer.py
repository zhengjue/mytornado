#!/usr/bin/env python
# _*_ coding:utf-8 _*-_
############################
# File Name: pageer.py
# Author: lza
# Created Time: 2016-08-15 14:30:08
############################


def try_page(currnet_page):
    try:
        current_page = int(current_page)
    except:
        current_page = 1


class PageInfo:
    def __inti__(self,current_page,all_count,pre_item=5):
        self.currentpage =  try_page(current_page)
        self.allcount = all_count
        self.preitem = pre_item

    @property
    def start(self):
        return (self.currentpage-1) * self.preitem

    @property
    def end(self):
        return self.currentpage * self.preitem

    @property
    def all_page_count(self):
        temp = divmod(self.allcount, self.preitem)
        if temp[1] == 0:
            all_page_count = temp[0]
        else:
            all_page_count = temp[0]+1
        return all_page_count

if __name__ == "__main__":
    pass

