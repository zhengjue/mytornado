from django.conf.urls import url
from autoadmin import views

urlpatterns = [
    url(r'^', views.Index),
    url(r'server_fun_categ/$', views.server_fun_categ),
    url(r'server_app_categ/$', views.server_app_categ),
    url(r'server_list/$', views.server_list),
    url(r'module_list/$', views.module_list),
    url(r'module_info/$', views.module_info),
    url(r'module_run/$', views.module_run),
    url(r'module_add/$', views.module_add),
    url(r'module_add_post/$', views.module_add_post),
]
