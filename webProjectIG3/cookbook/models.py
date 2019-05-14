# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	name = models.CharField(max_length = 100)
	recipe_text = models.TextField()
	number_of_people = models.IntegerField()

	def __str__(self):
		return self.name

class Ingredient(models.Model):
	name = models.CharField(max_length = 100, unique = True)

	def __str__(self):
		return self.name

class Contains(models.Model):
	ingredient = models.ForeignKey(Ingredient, on_delete = models.CASCADE)
	recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)
	unit = models.CharField(max_length = 100)
	quantity = models.IntegerField()

	class Meta:
		unique_together = ('ingredient', 'recipe')

class RecipeTag(models.Model):
	name = models.CharField(max_length = 100, unique = True)

	def __str__(self):
		return self.name

class Belongs(models.Model):
	recipeTag = models.ForeignKey(RecipeTag, on_delete = models.CASCADE)
	recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)

	class Meta:
		unique_together = ('recipeTag', 'recipe')

 






