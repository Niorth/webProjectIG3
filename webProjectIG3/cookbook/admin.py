# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Recipe
from .models import Contains
from .models import Ingredient
from .models import Belongs
from .models import RecipeTag

# Register your models here.

admin.site.register(Recipe)
admin.site.register(Contains)
admin.site.register(Ingredient)
admin.site.register(Belongs)
admin.site.register(RecipeTag)