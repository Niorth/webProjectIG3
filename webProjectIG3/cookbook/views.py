# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views import generic
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from cookbook.models import Ingredient
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, 'cookbook/index.html')

def loginView(request):
	return render(request, 'cookbook/login.html')

def accountView(request, user=None):
	if request.user.is_authenticated:
		if user is None:
			user = User.objects.get(username = request.user.get_username())

		username = user.username
		name = user.last_name
		firstname = user.first_name
		email = user.email
		return render(request, 'cookbook/account.html', { 
			"username" : username,
			"name" : name,
			"firstname" : firstname,
			"email" : email,
			})
	else:
		messages.warning(request, "Veuillez vous connecter")
		return HttpResponseRedirect(reverse('cookbook:login'))

def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('cookbook:index'))

def joinView(request):
	return render(request, 'cookbook/join.html')

def authentification(request):
	user = authenticate(username = request.POST['username'], password = request.POST['password'])
	if user is not None:
		login(request, user)
		return HttpResponseRedirect(reverse('cookbook:index'))
	else:
		messages.error(request, "Nom d'utilisateur ou mot de passe incorrecte")
		return HttpResponseRedirect(reverse('cookbook:login'))

def register(request):
	username = request.POST['username']
	name = request.POST['name']
	firstname = request.POST['firstname']
	email = request.POST['email']
	password = request.POST['password']

	if(username == "" or name == "" or firstname == "" or email == "" or password == ""):
		messages.error(request, "Veuillez remplir tous les champs")

		return HttpResponseRedirect(reverse('cookbook:join'))

	if(not(User.objects.filter(username = username).exists())):
		if(len(password) > 5):
			#create user
			user = User.objects.create_user(username, email, password)
			user.last_name = name
			user.first_name = firstname
			user.save()
			login(request, user)
			return HttpResponseRedirect(reverse('cookbook:index'))
		else:
			#wrong password
			messages.error(request, "Votre mot de passe doit contenir au moins 6 caracteres")

			return HttpResponseRedirect(reverse('cookbook:join'))
	else:
		#wrong username
		messages.error(request, "Nom d'utilisateur indisponible")

		return HttpResponseRedirect(reverse('cookbook:join'))

def modifyAccount(request):
	if request.user.is_authenticated:
		user = User.objects.get(username = request.user.get_username())
		fieldType = request.POST['type']
		fieldValue = request.POST['field']
		if(fieldType == 'username'):
			if(not(User.objects.filter(username = fieldValue).exists())):
				user.username = fieldValue
				messages.success(request, "Nom d'utilisateur modifié")
			else: 
				messages.error(request, "Nom d'utilisateur indisponible")

		elif(fieldType == 'name'):
			user.last_name = fieldValue
			messages.success(request, "Nom modifié")

		elif(fieldType == 'firstname'):
			user.first_name = fieldValue
			messages.success(request, "Prénom modifié")

		elif(fieldType == 'email'):
			user.email = fieldValue
			messages.success(request, "Email modifié")

		elif(fieldType == 'password'):
			if user.check_password(request.POST['oldPassword']):
				if(len(fieldValue) > 5):
					user.set_password(fieldValue);

					user.save()

					user = authenticate(username = request.user.get_username(), password = fieldValue)
					login(request, user)
					messages.success(request, 'mot de passe modifié')
				else:
					messages.error(request, "Votre mot de passe doit contenir au moins 6 caracteres")
			else:
				messages.error(request, 'Mot de passe incorrect')

		user.save()

		return accountView(request, user)

	else:
		return HttpResponseRedirect(reverse('cookbook:index'))

def createRecipe(request):
	return render(request, 'cookbook/createRecipe.html')

def saveRecipe(request):
	return render(request, 'cookbook/index.html')

def getAllIngredients(request):
    ingredients = Ingredient.objects.all()
    ingredientsName = []

    for i in range(len(ingredients)):
    	ingredientsName.append(ingredients[i].name)

    data = {
        'ingredientsName': ingredientsName
    }
    return JsonResponse(data)