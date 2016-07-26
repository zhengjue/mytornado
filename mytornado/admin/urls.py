# _*_ coding:utf-8 _*_
from admin import views

urlpatterns = [
        (r'/admin/check_user/?', views.CheckUserHandler),
        (r'/admin/change_user_info/([a-zA-Z0-9]+)/?', views.ChangeUserInfoHandler),
        (r'/admin/add_user/?', views.AddUserHandler),
        (r'/admin/user_list/?', views.AdminUserListHandler),
        (r'/admin/login/?', views.LoginHandler),
        (r'/admin/logout/?', views.LogoutHandler),
        (r'/admin/?', views.AdminHandler),
]
