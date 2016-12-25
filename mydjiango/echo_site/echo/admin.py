# _*_ coding:utf-8 _*_
from django.contrib import admin

# Register your models here.
from .models import Node, Line, Device

#对NodeAdmin进行个性化配置
#由于登记人的值我们希望能够自动记录相应登陆用户，因此在增加项目中取消登记人这一栏，并将登录用户作为登记人
class NodeAdmin(admin.ModelAdmin):
    #在list页面上显示指定的字段
    list_display = ('node_name','node_address','node_signer')
    #在编辑、新增页面上排除node_signer的选项
    exclude = ['node_signer']
    #对保存函数进行更改，将登录用户设置为登记人
    def save_model(self, request, obj, form, change):
        obj.node_signer = str(request.user)
        obj.save()


class LineAdmin(admin.ModelAdmin):
    #在编辑、新增页面上排除line_signer的选项
    exclude = ('line_signer',)
    #对保存函数进行更改，将登录用户设置为登记人
    def save_model(self, request, obj, form, change):
        obj.line_signer = str(request.user)
        obj.save()

class DeviceAdmin(admin.ModelAdmin):
    #在编辑、新增页面上排除device_signer的选项
    exclude = ('device_signer',)
    #对保存函数进行更改，将登录用户设置为登记人
    def save_model(self, request, obj, form, change):
        obj.device_signer = str(request.user)
        obj.save()

admin.site.register(Line,LineAdmin)
admin.site.register(Device,DeviceAdmin)
admin.site.register(Node,NodeAdmin)
