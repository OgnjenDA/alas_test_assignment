from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import contactSerializer, personSerializer, addressSerializer

from .models import Contact, Person, AddressEntry
from datetime import datetime

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'Contact List (Only active)':'/contacts/',
		'Person List (Only active)':'/persons/',
		'Contact CRUD':'/contacts/<str:pk>/',
		'Person CRUD':'/persons/<str:pk>/',
		'API LIST with is_older_than FILTER':'/addresses/',
		}
	return Response(api_urls)

# CONTACTS

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def contactList(request):
	if request.method == 'GET':
		contacts = Contact.objects.all().filter(active = True).order_by('-id')
		serializer = contactSerializer(contacts, many = True)
		return Response(serializer.data)
	elif request.method == 'POST':
		serializer = contactSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
		return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def contactDetail(request, pk):
	if request.method == 'GET':
		contacts = Contact.objects.get(id = pk)
		serializer = contactSerializer(contacts, many = False)
		return Response(serializer.data)
	elif request.method == 'PUT':
		contact = Contact.objects.get(id = pk)
		serializer = contactSerializer(instance = contact, data = request.data)
		if serializer.is_valid():
			serializer.save()
		return Response(serializer.data)
	elif request.method == 'DELETE':
		contacts = Contact.objects.get(id = pk)
		contacts.active = False
		contacts.save()
		serializer = contactSerializer(instance = contacts, data = request.data)
		if serializer.is_valid():
			serializer.save()
		return Response('Item successfully deleted. It is still there :)')			

# PERSONS

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def personList(request):
	if request.method == 'GET':
		persons = Person.objects.all().filter(active = True).order_by('-id')
		serializer = personSerializer(persons, many = True)
		return Response(serializer.data)
	elif request.method == 'POST':
		serializer = personSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
		return Response(serializer.data)
		

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def personDetail(request, pk):
	if request.method == 'GET':
		persons = Person.objects.get(id = pk)
		serializer = personSerializer(persons, many = False)
		return Response(serializer.data)
	elif request.method == 'PUT':
		person = Person.objects.get(id = pk)
		serializer = personSerializer(instance = person, data = request.data)
		if serializer.is_valid():
			serializer.save()
		return Response(serializer.data)
	elif request.method == 'DELETE':
		persons = Person.objects.get(id = pk)
		persons.active = False
		persons.save()
		serializer = personSerializer(instance = persons, data = request.data)
		if serializer.is_valid():
			serializer.save()
		return Response('Item successfully deleted. It is still there :)')		

# ADDRESSES WITH is_older_than FILTER

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAddressEntry(request):
	date_str = request.GET.get('is_older_than')
	if date_str:
		date = datetime.strptime(date_str, "%d-%m-%Y").date()
		addresses = AddressEntry.objects.filter(birthdate__gt = date)
	else:
		addresses = AddressEntry.objects.all()
	serializer = addressSerializer(addresses, many = True)
	return Response(serializer.data)