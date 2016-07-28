# _*_ coding:utf-8 _*_
from auth import views

urlpatterns = [
        (r'/register/?', views.RegisterHandler),
        (r'/login/?', views.LoginHandler),
        (r'/member/?', views.InfoHandler),
        (r'/transaction/([a-z]*)/?', views.TransactionHandler),
        (r'/transaction/review_list/?', views.ReviewHandler),
        (r'/jslogin/?', views.JsLoginHandler),
        (r'/logout/?', views.LogoutHandler),
]
