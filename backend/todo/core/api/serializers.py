from todo.core.base.models import Todo, DescrTodo
from rest_framework import serializers
from django.contrib.auth.models import User


class DescrTodoSerializer(serializers.ModelSerializer):	

	class Meta:
		model = DescrTodo
		fields = ("description", "update_date")


class TodoSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	descriptions = DescrTodoSerializer(many=True, required=False)

	class Meta:
		model = Todo
		fields = ("uuid" ,"value", "checked", "owner", "descriptions")

	def update(self, instance, validated_data):
		try:
			descr_data = validated_data.pop('descriptions')
		except KeyError:
			return 	super().update(instance, validated_data)
		for descr in descr_data:
			DescrTodo.objects.create(todo=instance, **descr)
		return super().update(instance, validated_data)


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ("uuid", "username")