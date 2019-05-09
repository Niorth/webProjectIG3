# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, 'cookbook/index.html')

def loginView(request):
	return render(request, 'cookbook/login.html')

def joinView(request):
	return render(request, 'cookbook/join.html')

def authentification(request):
	user = authenticate(username = request.POST['username'], password = request.POST['password'])
	if user is not None:
		login(request, user)
		return HttpResponseRedirect(reverse('cookbook:index'))

	else:
		return render(request, 'cookbook/login.html', {'error_message' : "Nom d'utilisateur ou mot de passe incorrecte"})

def register(request):
	username = request.POST['username']
	name = request.POST['name']
	firstname = request.POST['firstname']
	email = request.POST['email']
	password = request.POST['password']

	if(username == "" or name == "" or firstname == "" or email == "" or password == ""):
		return render(request, 'cookbook/join.html', {
			'error_message' : "Veuillez remplir tous les champs",
			'username' : username,
			'name' : name,
			'firstname' : firstname,
			'email' : email,
		})

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
			return render(request, 'cookbook/join.html', {
				'error_message' : "Votre mot de passe doit contenir au moins 6 caracteres",
				'username' : username,
				'name' : name,
				'firstname' : firstname,
				'email' : email,
				})
	else:
		#wrong username
		return render(request, 'cookbook/join.html', {
			'error_message' : "Nom d'utilisateur indisponible",
			'name' : name,
			'firstname' : firstname,
			'email' : email,
			})