#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from django.contrib import admin
from autoadmin import models

# Register your models here.

class ServerlistAdmin(admin.ModelAdmin):
    list_display = ('server_name','server_wip','server_lip','server_op','server_app_id') #admin中列表显示项
    search_fields = ('server_name','server_wip','server_lip','server_op','server_app_id') #添加搜索功能
    list_filter = ('server_name','server_wip','server_lip','server_op','server_app_id') #添加快速过滤功能

class ServerappAdmin(admin.ModelAdmin):
    list_display = ('server_categ_id','app_categ_name')
    search_fields = ('server_categ_id','app_categ_name')
    list_filter = ('server_categ_id','app_categ_name')

class ServerfunAdmin(admin.ModelAdmin):
    list_display = ('server_categ_name',)
    search_fields = ('server_categ_name',)
    list_filter = ('server_categ_name',)

class ModulelistAdmin(admin.ModelAdmin):
    list_display = ('module_name','module_caption','module_extend')
    search_fields = ('module_name','module_caption','module_extend')
    list_filter = ('module_name','module_caption','module_extend')



 #将模块添加到admin后台，进行可视化管理
admin.site.register(models.ServerFunCateg, ServerfunAdmin)
admin.site.register(models.ServerAppCateg, ServerappAdmin)
admin.site.register(models.ServerList, ServerlistAdmin)
admin.site.register(models.ModuleList, ModulelistAdmin)
