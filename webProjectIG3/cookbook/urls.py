from django.conf.urls import url

from . import views

app_name = 'cookbook'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^authentification/$', views.authentification, name='authentification'),
    url(r'^login/$', views.loginView, name='login'),
]