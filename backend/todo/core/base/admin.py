from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Todo, DescrTodo

def check_selected(modeladmin, request, queryset):
	queryset.update(checked=True)

class ArticleAdmin(admin.ModelAdmin):
    actions = [check_selected]
    

admin.site.register(User)
admin.site.register(Todo, ArticleAdmin)
admin.site.register(DescrTodo)