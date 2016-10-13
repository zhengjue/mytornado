#!/usr/bin/env python
# _*_ coding:utf-8 _*-_
############################
# File Name: forms.py
# Author: lza
# Created Time: 2016-09-26 15:01:18
############################

from django.forms import ModelForm
from .models import Node, Line, Device

#定义node Form ，form 名字为Model+ Form
class NodeForm(ModelForm):
    class Meta:
        #该ModelForm参照Model: Node
        model = Node
        #在Form中不显示node_signer这个字段
        exclude = ['node_siginer']

class LineForm(ModelForm):
    class Meta:
        model = Line
        exclude = ['line_signer']

class DeviceForm(ModelForm):
    class Meta:
        model = Device
        exclude = ['device_signer']

if __name__ == "__main__":
    pass

