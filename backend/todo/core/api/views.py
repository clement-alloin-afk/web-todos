from django.shortcuts import render
from rest_framework import permissions
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from todo.core.base.models import Todo
from .serializers import TodoSerializer	


class TodoList(generics.ListCreateAPIView):
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer
	permission_classes = (permissions.IsAuthenticated, )

	def get_queryset(self):
		user = self.request.user
		if not user.is_authenticated:
			return Todo.objects.none()
		return Todo.objects.filter(owner=user)
