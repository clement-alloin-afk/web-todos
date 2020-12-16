from django.test import TestCase
from rest_framework.test import RequestsClient
from django.urls import include, path, reverse


class TodoAPITest(TestCase):
	def test_izi(self):
		x = 1
		self.assertEqual(1, x)

	def test_connexion(self) :
		response = self.client.post('/api/token/' , {"username": "visitor", "password": "visitor"})
		self.assertEqual(response.status_code, 200, response)

	def test_mauvais_id(self):
		response = self.client.post('/api/token/' , {"username": "mauvais", "password": "faux"})
		self.assertEqual(response.status_code, 401, response)

	def test_not_connected(self):
		response = self.client.get('/api/todos/')
		self.assertEqual(response.status_code, 401, response)



#self.assertEqual(response.data.get('non_field_errors'), ['No active account found with the given credentials'])