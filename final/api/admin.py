from django.contrib import admin

from .models import AddressEntry, Person, Contact

admin.site.register(AddressEntry)
admin.site.register(Person)
admin.site.register(Contact)