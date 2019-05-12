from django.conf.urls import url

from . import views

app_name = 'cookbook'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^authentification/$', views.authentification, name='authentification'),
    url(r'^login/$', views.loginView, name='login'),
    url(r'^join/$', views.joinView, name='join'),
	url(r'^logout/$', views.logoutView, name='logout'),    
	url(r'^register/$', views.register, name='register'),
	url(r'^account/$', views.accountView, name='account'), 
	url(r'^modifyAccount/$', views.modifyAccount, name='modifyAccount'),   
	url(r'^createRecipe/$', views.createRecipe, name='createRecipe'),  
	url(r'^saveRecipe/$', views.saveRecipe, name='saveRecipe'), 
	url(r'^getAllIngredients/$', views.getAllIngredients, name='getAllIngredients'), 
]