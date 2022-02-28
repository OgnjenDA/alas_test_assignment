from django.db import models
from django.utils import timezone


class AddressEntry(models.Model):
	gender_choices = (('Male', 'Male'),
					  ('Female', 'Female'))

	gender = models.CharField(max_length = 6, choices = gender_choices, default = 'Male')
	name = models.CharField(max_length = 50)
	firstname = models.CharField(max_length = 50)
	birthdate = models.DateField(default = timezone.now)
	active = models.BooleanField(default = True, blank = True, null = False)

class Person(AddressEntry):
	def __str__(self):
		return self.name

class Contact(AddressEntry):
	#phone_number = models.CharField(max_length=20, blank=True, null=True)
	def __str__(self):
		return self.name