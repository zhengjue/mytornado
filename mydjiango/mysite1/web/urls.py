from django.conf.urls import url
from django.contrib import admin
from web import views
urlpatterns = [
    #  url(r'^admin/', admin.site.urls),
    url(r'^login/', views.login),
]
