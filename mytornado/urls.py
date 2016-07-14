# _*_ coding:utf-8 _*_
import auth.urls
import admin.urls
import index


urlpatterns = [
    (r"/?", index.IndexHandler),
]

urlpatterns += auth.urls.urlpatterns + admin.urls.urlpatterns

