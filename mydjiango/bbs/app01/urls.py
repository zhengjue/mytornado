from django.conf.urls import url
from django.contrib import admin
from app01 import views
urlpatterns = [
    #  url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^addfavor/', views.addfavor),
    url(r'^getreply/', views.getreply),
    url(r'^addreply/', views.addreply),
]
