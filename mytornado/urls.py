# _*_ coding:utf-8 _*_
import auth.urls
import index


urlpatterns = [
    (r"/?", index.IndexHandler),
]

urlpatterns += auth.urls.urlpatterns

