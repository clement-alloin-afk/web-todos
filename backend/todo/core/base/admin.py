from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Todo, DescrTodo

my_models = [User, Todo, DescrTodo]

admin.site.register(my_models)