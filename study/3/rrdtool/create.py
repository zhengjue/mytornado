#!/usr/bin/env python
# _*_ coding:utf-8 _*-_
############################
# File Name: create.py
# Author: lza
# Created Time: 2016-09-02 13:35:45
############################
import rrdtool
import time

cur_time = str(int(time.time()))   # 获取当前Linux时间戳作为rrd起始时间
# 数据写频率--step为300秒 (即5分钟一个数据点)
rrd = rrdtool.create(
    'Flow.rrd',
    '--step', '300',  # 指定rrdtool每隔多长时间就收到一个值，默认为5分钟
    '--start', cur_time,  # 指定rrdtool第一条记录的起始时间，必须是timestamp的格式；

    # DT 定义数据源eth0_in (入流量)、eth0_out (出流量)用于定义数据源，用于存放脚本的结果的变量；
    # 类型都为COUNTER (递增)；
    # 600秒为心跳值,其含义是600秒没有收到值, 则会用UNKNOWN代替；
    # 0为最小值；最大值用U代替, 表示不确定
    'DS:eth0_in:COUNTER:600:0:U',
    'DS:eth0_out:COUNTER:600:0:U',

    # RRA定义格式为[RRA:CF:xff:steps:rows],
    # CF定义了AVERAGE、MAX、MIN三种数据合并方式
    # xff定义为0.5, 表示一个CDP中的PDP值如超过一半值为UNKNOWN, 则该CDP的值就被标为UNKNOWN
    # 下列前4个RRA的定义说明如下, 其他定义与AVERAGE方式相似,
    # 区别是存最大值与最小值
    # 每隔5分钟 (1*300秒)存一次数据的平均值, 存600笔, 即2.08天
    # 每隔30分钟 (6*300秒)存一次数据的平均值, 存700笔, 即14.58天 (2周)
    # 每隔2小时 (24*300秒)存一次数据的平均值, 存775笔, 即64.58天 (2个月)
    # 每隔24小时 (288*300秒)存一次数据的平均值, 存797笔, 即797天 (2年)

    'RRA:AVERAGE:0.5:1:600',
    'RRA:AVERAGE:0.5:6:700',
    'RRA:AVERAGE:0.5:24:775',
    'RRA:AVERAGE:0.5:288:797',
    'RRA:MAX:0.5:1:600',
    'RRA:MAX:0.5:6:700',
    'RRA:MAX:0.5:24:775',
    'RRA:MAX:0.5:444:797',
    'RRA:MIN:0.5:1:600',
    'RRA:MIN:0.5:6:700',
    'RRA:MIN:0.5:24:775',
    'RRA:MIN:0.5:444:797'
)
if rrd:
    print rrdtool.error()


if __name__ == "__main__":
    pass

