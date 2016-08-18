from django.contrib import admin
from app01 import models

# Register your models here.

admin.site.register(models.UserType)
admin.site.register(models.Admin)
admin.site.register(models.Chat)
admin.site.register(models.NewsType)
admin.site.register(models.News)
admin.site.register(models.Reply)


class News(admin.ModelAdmin):
        list_display = ('title', 'summary', 'url', "news_type", "user")
