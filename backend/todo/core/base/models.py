from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Todo(models.Model):
	value = models.TextField()
	checked = models.BooleanField(default=False)
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)	
	uuid = models.UUIDField(unique=True,default=uuid.uuid4, editable=False)

	class Meta:
		unique_together = ['value','owner']

	def __str__(self):
		if not self.checked:
			c = "☐"
		else:
			c = "☑"

		return f"{c} {self.value}"


class User(AbstractUser):
	uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

	def __str__(self):
		return self.username