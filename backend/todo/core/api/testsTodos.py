from django.test import TestCase
from todo.core.base.models import User
from rest_framework.test import APIClient, force_authenticate
from django.urls import include, path, reverse

class TodoAPITest(TestCase):

	def setUp(self):
		self.userTest = User.objects.create_user(username="userTest", password="userTest")
		self.client = APIClient()
		self.client.force_authenticate(user=self.userTest)
	
	def test_ajout_Todo(self):
		response = self.client.post('/api/todos/', { 'value': 'Test Backend' , 'checked': 'false' })
		self.assertEqual(response.status_code, 201)

	def test_ajout_Todos(self):
		response1 = self.client.post('/api/todos/', { 'value': 'Test multiple 1' , 'checked': 'false' })
		response2 = self.client.post('/api/todos/', { 'value': 'Test multiple 2' , 'checked': 'false' })
		self.assertEqual(response1.status_code, 201)
		self.assertEqual(response2.status_code, 201)

		response = self.client.get('/api/todos/')
		self.assertEqual(len(response.data), 2, response.data)

	def test_recuperer_un_todo(self):
		self.client.post('/api/todos/', { 'value': 'Test recup' , 'checked': 'false' })
		response = self.client.get('/api/todos/')
		todo1 = self.client.get('/api/todo/'+response.data[0]['uuid']+"/")
		self.assertEqual(todo1.data['value'], 'Test recup')

	def test_delete_todo(self):
		#Ajout de 2 todos
		self.client.post('/api/todos/', { 'value': 'Ajout delete 1' , 'checked': 'false' })
		self.client.post('/api/todos/', { 'value': 'Ajout delete 2' , 'checked': 'false' })
		response = self.client.get('/api/todos/')
		#on a bien les 2 todos
		self.assertEqual(len(response.data), 2)

		#je supprime le premier
		responseDelete = self.client.delete('/api/todo/'+response.data[0]['uuid']+'/')
		self.assertEqual(responseDelete.status_code, 204)
		# On en a plus qu'un
		response = self.client.get('/api/todos/')
		self.assertEqual(len(response.data), 1)

	def test_modif_value(self):
		self.client.post('/api/todos/', { 'value': 'Modif' , 'checked': 'false' })
		response = self.client.get('/api/todos/')
		responseModif = self.client.patch('/api/todo/'+response.data[0]['uuid']+'/', {'value':'Le test bg'})

		response = self.client.get('/api/todos/')
		self.assertEqual(responseModif.status_code, 200) 
		self.assertEqual(response.data[0]['value'], 'Le test bg')

	def test_check_Todo(self):
		#J'ajoute un todo et vérifie qu'il est pas check
		self.client.post('/api/todos/', { 'value': 'Check/Uncheck' , 'checked': 'false' })
		response = self.client.get('/api/todos/')
		responseTodo = self.client.get('/api/todo/'+response.data[0]['uuid']+'/')
		responseCheck = responseTodo.data['checked']
		self.assertFalse(responseCheck)

		#Je le check
		responseChange = self.client.patch('/api/todo/'+responseTodo.data['uuid']+'/', {'checked':'true'})
		self.assertEqual(responseChange.status_code, 200)

		#Je vérifie qu'il est checker
		response = self.client.get('/api/todos/')
		responseTodo = self.client.get('/api/todo/'+response.data[0]['uuid']+'/')
		responseCheck = responseTodo.data['checked']
		self.assertTrue(responseCheck)