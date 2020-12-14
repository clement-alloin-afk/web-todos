from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Todo

my_models = [User, Todo]

admin.site.register(my_models)