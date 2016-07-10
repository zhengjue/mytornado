# _*_ coding:utf-8 _*_
from auth import views

urlpatterns = [
        (r'/register/?', views.RegisterHandler),
        (r'/login/?', views.LoginHandler),
        (r'/logout/?', views.LogoutHandler),
]
