from django.conf.urls import url

from . import views

app_name = 'cookbook'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.loginView, name='login'),
    url(r'^join/$', views.joinView, name='join'),
	url(r'^logout/$', views.logoutView, name='logout'),    
	url(r'^account/$', views.accountView, name='account'), 
	url(r'^createRecipe/$', views.createRecipe, name='createRecipe'),  
	url(r'^recipes/$', views.allRecipes, name='recipes'), 
	url(r'^getAllIngredients/$', views.getAllIngredients, name='getAllIngredients'), 
	url(r'^getAllTags/$', views.getAllTags, name='getAllTags'), 
	url(r'^recipe/(?P<recipe_id>[0-9]+)/$', views.recipe, name='recipe'), 
	url(r'^deleteRecipe/(?P<recipe_id>[0-9]+)/$', views.deleteRecipe, name='deleteRecipe'),
	url(r'^updateRecipe/(?P<recipe_id>[0-9]+)/$', views.updateRecipe, name='updateRecipe'),

]