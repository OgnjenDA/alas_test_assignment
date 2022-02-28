import json
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from django.test import TestCase
from rest_framework import status
from .models import AddressEntry, Contact, Person
from .serializers import contactSerializer
from django.contrib.auth.models import User
from django.test import Client


class  modelTestCase(TestCase):

	def test_modelContact(self):
		contact = Contact(gender = 'Male', 
							name = 'Ogi',
							firstname = 'Ognjen', 
							birthdate = '2021-05-22', 
							active = True)

		self.assertEqual(contact.gender, 'Male')
		self.assertEqual(contact.name, 'Ogi')
		self.assertEqual(contact.firstname, 'Ognjen')
		self.assertEqual(contact.birthdate, '2021-05-22')
		self.assertEqual(contact.active, True)

	def test_modelPerson(self):
		person = Person(gender = 'Male', 
							name = 'Ogi',
							firstname = 'Ognjen', 
							birthdate = '2021-05-22', 
							active = True)

		self.assertEqual(person.gender, 'Male')
		self.assertEqual(person.name, 'Ogi')
		self.assertEqual(person.firstname, 'Ognjen')
		self.assertEqual(person.birthdate, '2021-05-22')
		self.assertEqual(person.active, True)

	def test_modelAddressEntry(self):
		address_entry = AddressEntry(gender = 'Male', 
							name = 'Ogi',
							firstname = 'Ognjen', 
							birthdate = '2021-05-22', 
							active = True)

		self.assertEqual(address_entry.gender, 'Male')
		self.assertEqual(address_entry.name, 'Ogi')
		self.assertEqual(address_entry.firstname, 'Ognjen')
		self.assertEqual(address_entry.birthdate, '2021-05-22')
		self.assertEqual(address_entry.active, True)


class  APITestCase(APITestCase): 

	def setUp(self):
		self.user = User.objects.create_user(username = "test", password = "test") 

	def test_contactCreate(self):

		# Not authorized
		contact ={
       		"gender": "Male",
       		"name": "Ogi",
       		"firstname": "Ognjen",
       		"birthdate": "2021-05-22",
       		"active": True
			}
		response = self.client.post('/api/contacts/', contact)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

		# Authorized
		self.client.force_authenticate(user = self.user)
		contact ={
       		"gender": "Male",
       		"name": "Ogi",
       		"firstname": "Ognjen",
       		"birthdate": "2021-05-22",
       		"active": True
			}
		response = self.client.post('/api/contacts/', contact)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		response = self.client.post('/api/contacts', contact)
		self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

	def test_personCreate(self):

		# Not authorized
		person ={
       		"gender": "Male",
       		"name": "Ogi",
       		"firstname": "Ognjen",
       		"birthdate": "2021-05-22",
       		"active": True
			}
		response = self.client.post('/api/persons/', person)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

		# Authorized
		self.client.force_authenticate(user = self.user)
		person ={
       		"gender": "Male",
       		"name": "Ogi",
       		"firstname": "Ognjen",
       		"birthdate": "2021-05-22",
       		"active": True
			}
		response = self.client.post('/api/persons/', person)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		response = self.client.post('/api/persons', person)
		self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

	def test_contactList(self):

		# Not authorized
		contact ={
       		"gender": "Male",
       		"name": "Ogi",
       		"firstname": "Ognjen",
       		"birthdate": "2021-05-22",
       		"active": True
			}
		response = self.client.get('/api/contacts/', contact)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

		# Authorized
		self.client.force_authenticate(user = self.user)
		contact ={
       		"gender": "Male",
       		"name": "Ogi",
       		"firstname": "Ognjen",
       		"birthdate": "2021-05-22",
       		"active": True
			}
		response = self.client.get('/api/contacts/', contact)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		response = self.client.get('/api/contacts', contact)
		self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

	def test_personList(self):

		# Not authorized
		person ={
       		"gender": "Male",
       		"name": "Ogi",
       		"firstname": "Ognjen",
       		"birthdate": "2021-05-22",
       		"active": True
			}
		response = self.client.get('/api/persons/', person)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

		# Authorized
		self.client.force_authenticate(user = self.user)
		person ={
       		"gender": "Male",
       		"name": "Ogi",
       		"firstname": "Ognjen",
       		"birthdate": "2021-05-22",
       		"active": True
			}
		response = self.client.get('/api/persons/', person)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		response = self.client.get('/api/persons', person)
		self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

	def test_Update(self):

		# Not authorized (Contact)
		self.contact = Contact.objects.create(gender = "Male",
       											name = "Ogi",
       											firstname = "Ognjen",
       											birthdate =  "2021-05-22",
       											active = True)
		response = self.client.put('/api/contacts/1/', kwargs={'pk': self.contact.pk})
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

		# Not authorized (Person)
		self.person = Person.objects.create(gender = "Male",
       											name = "Ogi",
       											firstname = "Ognjen",
       											birthdate =  "2021-05-22",
       											active = True)
		response = self.client.put('/api/persons/1/', kwargs={'pk': self.person.pk})
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

		# Authorized (Contact)
		self.client.force_authenticate(user = self.user)
		self.contact = Contact.objects.create(gender = "Male",
       											name = "Ogi",
       											firstname = "Ognjen",
       											birthdate =  "2021-05-22",
       											active = True)
		response = self.client.put('/api/contacts/1/', kwargs={'pk': self.contact.pk})
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		response = self.client.put('/api/contacts/1', kwargs={'pk': self.contact.pk})
		self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

		# Authorized (Person)
		self.client.force_authenticate(user = self.user)
		self.person = Person.objects.create(gender = "Male",
       											name = "Ogi",
       											firstname = "Ognjen",
       											birthdate =  "2021-05-22",
       											active = True)
		response = self.client.put('/api/persons/1/', kwargs={'pk': self.person.pk})
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		response = self.client.put('/api/persons/1', kwargs={'pk': self.person.pk})
		self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

	def test_Detail(self):

		# Not authorized (Contact)
		self.contact = Contact.objects.create(gender = "Male",
       											name = "Ogi",
       											firstname = "Ognjen",
       											birthdate =  "2021-05-22",
       											active = True)
		response = self.client.get('/api/contacts/1/', kwargs={'pk': self.contact.pk})
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

		# Not authorized (Person)
		self.person = Person.objects.create(gender = "Male",
       											name = "Ogi",
       											firstname = "Ognjen",
       											birthdate =  "2021-05-22",
       											active = True)
		response = self.client.get('/api/persons/1/', kwargs={'pk': self.person.pk})
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

		# Authorized (Contact)
		self.client.force_authenticate(user = self.user)
		self.contact = Contact.objects.create(gender = "Male",
       											name = "Ogi",
       											firstname = "Ognjen",
       											birthdate =  "2021-05-22",
       											active = True)
		response = self.client.get('/api/contacts/1/', kwargs={'pk': self.contact.pk})
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		response = self.client.get('/api/contacts/1', kwargs={'pk': self.contact.pk})
		self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

		# Authorized (Person)
		self.client.force_authenticate(user = self.user)
		self.person = Person.objects.create(gender = "Male",
       											name = "Ogi",
       											firstname = "Ognjen",
       											birthdate =  "2021-05-22",
       											active = True)
		response = self.client.get('/api/persons/1/', kwargs={'pk': self.person.pk})
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		response = self.client.get('/api/persons/1', kwargs={'pk': self.person.pk})
		self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

	def test_Delete(self):

		# Not authorized (Contact)
		self.contact = Contact.objects.create(gender = "Male",
       											name = "Ogi",
       											firstname = "Ognjen",
       											birthdate =  "2021-05-22",
       											active = True)
		response = self.client.delete('/api/contacts/1/', kwargs={'pk': self.contact.pk})
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

		# Not authorized (Person)
		self.person = Person.objects.create(gender = "Male",
       											name = "Ogi",
       											firstname = "Ognjen",
       											birthdate =  "2021-05-22",
       											active = True)
		response = self.client.delete('/api/persons/1/', kwargs={'pk': self.person.pk})
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

		# Authorized (Contact)
		self.client.force_authenticate(user = self.user)
		self.contact = Contact.objects.create(gender = "Male",
       											name = "Ogi",
       											firstname = "Ognjen",
       											birthdate =  "2021-05-22",
       											active = True)
		response = self.client.delete('/api/contacts/1/', kwargs={'pk': self.contact.pk})
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		response = self.client.delete('/api/contacts/1', kwargs={'pk': self.contact.pk})
		self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)
		response = self.client.get('/api/contacts/1/', kwargs={'pk': self.contact.pk})
		self.assertEqual(self.contact.gender, 'Male')
		self.assertEqual(self.contact.name, 'Ogi')
		self.assertEqual(self.contact.firstname, 'Ognjen')
		self.assertEqual(self.contact.birthdate, '2021-05-22')
		self.assertEqual(self.contact.active, False)


		# Authorized (Person)
		self.client.force_authenticate(user = self.user)
		self.person = Person.objects.create(gender = "Male",
       											name = "Ogi",
       											firstname = "Ognjen",
       											birthdate =  "2021-05-22",
       											active = True)
		response = self.client.delete('/api/persons/1/', kwargs={'pk': self.person.pk})
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		response = self.client.delete('/api/persons/1', kwargs={'pk': self.person.pk})
		self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)