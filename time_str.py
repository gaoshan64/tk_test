# !/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# @Time : 2020/6/19 8:10
# @Author : gaoshan
# @Email : gaoshan-1@michelin.com
# @File : time_str.py
# @Software: PyCharm
# ----------------------------------------------------------------
# ----------------------------------------------------------------

# ----------------------------------------------------------------
from datetime import datetime


def get_time_str():
    time = datetime.now()
    time_str = '{}_{}_{}_{}_{}_{}'.format(time.year, time.month, time.day, time.hour, time.minute, time.second)
    return time_str


if __name__ == '__main__':
    time_str = get_time_str()
    print(time_str)
