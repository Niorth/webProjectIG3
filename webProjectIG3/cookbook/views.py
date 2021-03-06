# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views import generic
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from cookbook.models import Ingredient, RecipeTag, Recipe, Belongs, Contains
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, 'cookbook/index.html')

def loginView(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('cookbook:index'))
	else:
		if request.method == 'GET':
			return render(request, 'cookbook/login.html')
		else:
			user = authenticate(username = request.POST['username'], password = request.POST['password'])
			if user is not None:
				login(request, user)
				return HttpResponseRedirect(reverse('cookbook:index'))
			else:
				messages.error(request, "Nom d'utilisateur ou mot de passe incorrecte")
				return HttpResponseRedirect(reverse('cookbook:login'))

def accountView(request, user=None):
	if request.user.is_authenticated:
		if request.method == 'GET':
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
			return HttpResponseRedirect(reverse('cookbook:account'))

	else:
		messages.warning(request, "Veuillez vous connecter")
		return HttpResponseRedirect(reverse('cookbook:login'))

def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('cookbook:index'))

def joinView(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('cookbook:index'))
	else:
		if request.method == 'GET':
			return render(request, 'cookbook/join.html')
		else:
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

def createRecipe(request):
	if request.user.is_authenticated:
		if request.method=='POST':

			name = request.POST["name"]
			recipe_text = request.POST["recipe_text"]
			nb_people = request.POST["nb_people"]
			ingredients = request.POST.getlist("ingredients[]")
			unit = request.POST.getlist("unit[]")
			qty = request.POST.getlist("qty[]")
			tags = request.POST.getlist("tags[]")


			i = 0
			while i < len(ingredients):
				if not Ingredient.objects.filter(name = ingredients[i]).exists():
					del ingredients[i]
					del unit[i]
					del qty[i]
				else:
					i+=1

			j = 0
			while j < len(tags):
				if not RecipeTag.objects.filter(name = tags[j]).exists():
					del tags[j]
				else:
					j+=1
					
			if name and recipe_text and nb_people and ingredients and unit and qty:
				if len(ingredients) == len(unit) and len(unit) == len(qty):
					if int(nb_people) > 0:
						user = User.objects.get(username = request.user.get_username())
						recipe = Recipe(user = user, name = name, recipe_text = recipe_text, number_of_people = int(nb_people))
						recipe.save()

						for i in range(len(ingredients)):
							contains = Contains(
								ingredient = Ingredient.objects.get(name = ingredients[i]),
								unit = unit[i],
								quantity = int(qty[i]),
								recipe = recipe)
							contains.save()

						for i in range(len(tags)):
							belongs = Belongs(recipeTag = RecipeTag.objects.get(name = tags[i]), recipe = recipe)
							belongs.save()

						return JsonResponse({"success" : True, "url" : reverse("cookbook:createRecipe")})
					else:
						return JsonResponse({"success" : False, "message" : "Nombre de personne invalide"})
				else:
					return JsonResponse({"success" : False, "message" : "Une erreur est survenue sur la liste d'ingrédients"})
			else:
				return JsonResponse({"success" : False, "message" : "Veuillez remplir les champs obligatoires correctement"})

						
		
		else:
			return render(request, 'cookbook/createRecipe.html')
	else:
		messages.warning(request, "Veuillez vous connecter")
		return HttpResponseRedirect(reverse('cookbook:login'))

def getAllIngredients(request):
    ingredients = Ingredient.objects.all()
    ingredientsName = []

    for i in range(len(ingredients)):
    	ingredientsName.append(ingredients[i].name)

    data = {
        'ingredientsName': ingredientsName
    }
    return JsonResponse(data)

def getAllTags(request):
    tags = RecipeTag.objects.all()
    tagsName = []

    for i in range(len(tags)):
    	tagsName.append(tags[i].name)

    data = {
        'tagsName': tagsName
    }
    return JsonResponse(data)

def getAllRecipes(request):
    recipes = Recipe.objects.all()
    recipesName = []

    for i in range(len(recipes)):
    	recipesName.append(recipes[i].name)

    data = {
        'recipesName': recipesName
    }
    return JsonResponse(data)

def getRecipeByName(request):
	if request.user.is_authenticated:
		if request.method=='GET':
			name = request.GET["name"]
			if Recipe.objects.filter(name = name, user = User.objects.get(username = request.user.get_username())).exists():
				recipeId = Recipe.objects.filter(name = name, user = User.objects.get(username = request.user.get_username()))[0].id
				return recipe(request, recipeId)
			else:
				return render(request, 'cookbook/noRecipe.html')

def allRecipes(request):
	if request.user.is_authenticated:
		if request.method=='GET':
			allRecipes = Recipe.objects.filter(user = User.objects.get(username = request.user.get_username()))				

			return render(request, 'cookbook/recipes.html', {"recipes":allRecipes})
	else:
		messages.warning(request, "Veuillez vous connecter")
		return HttpResponseRedirect(reverse('cookbook:login'))

def recipe(request, recipe_id):
	if request.user.is_authenticated:
		if request.method=='GET':
			if request.user == Recipe.objects.get(id = recipe_id).user:
				recipe = Recipe.objects.get(id = recipe_id)
				ingredients = Contains.objects.filter(recipe = recipe_id)
				tags = Belongs.objects.filter(recipe = recipe_id)

				context = {"recipe" : recipe, "ingredients" : ingredients, "tags" : tags}
				return render(request, 'cookbook/recipe.html', context)
			else:
				HttpResponseRedirect(reverse('cookbook:index'))
		else:
			HttpResponseRedirect(reverse('cookbook:index'))
	else:
		messages.warning(request, "Veuillez vous connecter")
		HttpResponseRedirect(reverse('cookbook:login'))

def deleteRecipe(request, recipe_id):
	if request.user.is_authenticated:
		if request.user == Recipe.objects.get(id = recipe_id).user:
			Recipe.objects.get(id = recipe_id).delete()
			return HttpResponseRedirect(reverse('cookbook:recipes'))
		else:
			return HttpResponseRedirect(reverse('cookbook:recipes'))
	else:
		messages.warning(request, "Veuillez vous connecter")
		return HttpResponseRedirect(reverse('cookbook:login'))

def updateRecipe(request, recipe_id):
	if request.user.is_authenticated:
		if request.user == Recipe.objects.get(id = recipe_id).user:
			if request.method=='GET':
			
				recipe = Recipe.objects.get(id = recipe_id)
				ingredientsList = Contains.objects.filter(recipe = recipe_id)
				ingredients = []
				tags = Belongs.objects.filter(recipe = recipe_id)

				for i in range(len(ingredientsList)):
					obj = {"id" : i, "ingredient" : ingredientsList[i]}
					ingredients.append(obj)

				context = {"recipe" : recipe, "ingredients" : ingredients, "tags" : tags, "nbIngredients" : len(ingredients), "updateRecipe" : True}
				return render(request, 'cookbook/createRecipe.html', context)

			else:
				name = request.POST["name"]
				recipe_text = request.POST["recipe_text"]
				nb_people = request.POST["nb_people"]
				ingredients = request.POST.getlist("ingredients[]")
				unit = request.POST.getlist("unit[]")
				qty = request.POST.getlist("qty[]")
				tags = request.POST.getlist("tags[]")

				i = 0
				while i < len(ingredients):
					if not Ingredient.objects.filter(name = ingredients[i]).exists():
						del ingredients[i]
						del unit[i]
						del qty[i]
					else:
						i+=1

				j = 0
				while j < len(tags):
					if not RecipeTag.objects.filter(name = tags[j]).exists():
						del tags[j]
					else:
						j+=1
						
				if name and recipe_text and nb_people and ingredients and unit and qty:
					if len(ingredients) == len(unit) and len(unit) == len(qty):
						if int(nb_people) > 0:
							recipe = Recipe.objects.get(id = recipe_id)
							recipe.name = name
							recipe.recipe_text = recipe_text
							recipe.number_of_people = nb_people

							recipe.save()

							Contains.objects.filter(recipe = recipe).delete()
							Belongs.objects.filter(recipe = recipe).delete()

							for i in range(len(ingredients)):
								contains = Contains(
									ingredient = Ingredient.objects.get(name = ingredients[i]),
									unit = unit[i],
									quantity = int(qty[i]),
									recipe = recipe)
								contains.save()

							for i in range(len(tags)):
								belongs = Belongs(recipeTag = RecipeTag.objects.get(name = tags[i]), recipe = recipe)
								belongs.save()

							return JsonResponse({"success" : True, "url" : reverse("cookbook:recipe", kwargs={'recipe_id': recipe_id})})
						else:
							return JsonResponse({"success" : False, "message" : "Nombre de personne invalide"})
					else:
						return JsonResponse({"success" : False, "message" : "Une erreur est survenue sur la liste d'ingrédients"})
				else:
					return JsonResponse({"success" : False, "message" : "Veuillez remplir les champs obligatoires correctement"})
		else:
			return HttpResponseRedirect(reverse('cookbook:index'))
	else:
		messages.warning(request, "Veuillez vous connecter")
		return HttpResponseRedirect(reverse('cookbook:login'))


