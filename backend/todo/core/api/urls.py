from django.contrib import admin
from django.urls import path
from .views import TodoList
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url

schema_view = get_swagger_view(title='Mon API')

urlpatterns = [
    path("todos/", TodoList.as_view(), name="todo_list"),
    path("todo/<uuid:uuid>", TodoList.as_view(), name="todo_list"),	
    url(r'^$', schema_view),
]



'''
GET /todos: liste les todos

GET /todo/<uid>: affiche le todo dont l'uid est uid

POST /todos: ajoute un todo

PATCH /todo/<uid>: modifie le todo dont l'uid est uid

DELETE /todo/<uid>: supprime le todo dont l'uid est uid
'''