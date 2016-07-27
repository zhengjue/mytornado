# _*_ coding:utf-8 _*_
from admin import views

urlpatterns = [
        (r'/admin/login/?', views.LoginHandler),
        (r'/admin/logout/?', views.LogoutHandler),
        (r'/admin/?', views.AdminHandler),
]
