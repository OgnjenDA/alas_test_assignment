from rest_framework import serializers
from .models import AddressEntry, Contact, Person

class contactSerializer(serializers.ModelSerializer):
	class Meta:
		model = Contact
		fields ='__all__'

class personSerializer(serializers.ModelSerializer):
	class Meta:
		model = Person
		fields ='__all__'

class addressSerializer(serializers.ModelSerializer):
	class Meta:
		model = AddressEntry
		fields ='__all__'