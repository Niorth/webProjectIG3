# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth import authenticate, login
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, 'cookbook/index.html')

def loginView(request):
	return render(request, 'cookbook/login.html')

def authentification(request):
	user = authenticate(username = request.POST['username'], password = request.POST['password'])
	if user is not None:
		login(request, user)
		return HttpResponseRedirect(reverse('cookbook:index'))

	else:
		return render(request, 'cookbook/login.html', {'error_message' : "Nom d'utilisateur ou mot de passe incorrecte"})
