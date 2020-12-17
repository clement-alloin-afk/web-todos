from django.test import TestCase
from todo.core.base.models import User
from rest_framework.test import RequestsClient
from django.urls import include, path, reverse

class TodoAPITest(TestCase):
	def setUp(self):
		self.userTest = User.objects.create_user(username="userTest", password="userTest")

	def test_connexion_bons_identifiants(self) :
		response = self.client.post('/api/token/' , {"username": "userTest", "password": "userTest"}, format="json")
		self.assertEqual(response.status_code, 200)
		token = response.data['access']
		self.assertIsNotNone(token)

	def test_sans_identifiants(self):
		response = self.client.post('/api/token/')
		self.assertEqual(response.status_code, 400)

	def test_sans_username(self):
		response = self.client.post('/api/token/')
		self.assertEqual(response.status_code, 400)

	def test_sans_password(self):
		response = self.client.post('/api/token/')
		self.assertEqual(response.status_code, 400)

	def test_mauvais_identifiants(self):
		response = self.client.post('/api/token/' , {"username": "mauvais", "password": "faux"})
		self.assertEqual(response.status_code, 401)

	def test_not_connected(self):
		response = self.client.get('/api/todos/')
		self.assertEqual(response.status_code, 401)
