from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Todo, DescrTodo

def check_selected(modeladmin, request, queryset):
	queryset.update(checked=true)


class ArticleAdmin(admin.ModelAdmin):
    actions = [check_selected]

my_models = [User, Todo, DescrTodo]

admin.site.register(my_models)