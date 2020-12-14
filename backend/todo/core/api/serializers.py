from todo.core.base.models import Todo
from rest_framework import serializers
from django.contrib.auth.models import User


class TodoSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Todo
		fields = ("uuid" ,"value", "checked", "owner")


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ("uuid", "username")