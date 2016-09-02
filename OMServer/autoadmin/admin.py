from django.contrib import admin

# Register your models here.
from django.contrib import admin
from autoadmin.models import *


admin.site.register(ServerFunCateg)
admin.site.register(ServerAppCateg)
admin.site.register(ServerList)
admin.site.register(ModuleList)


class ServerAppCateg(admin.ModelAdmin):
    list_display = ("server_categ_id", "app_categ_name")


class ServerFunCateg(admin.ModelAdmin):
    list_display = ("server_categ_name")


class ServerList(admin.ModelAdmin):
    list_display = ("server_name", "server_wip", "server_lip", "server_op", "server_app_id")


class ModuleList(admin.ModelAdmin):
    list_display = ("module_name", "module_caption", "module_extend")
