from django.conf.urls import url
from django.contrib import admin
from app01 import views
urlpatterns = [
    #  url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^login/', views.login),
    url(r'^addfavor/', views.addfavor),
    url(r'^getreply/', views.getreply),
    url(r'^getchat/', views.getchat),
    url(r'^getchat2/', views.getchat2),
    url(r'^addreply/', views.addreply),
    url(r'^addmsg/', views.addmsg),
]
