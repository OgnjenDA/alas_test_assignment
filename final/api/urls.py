from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name = "api-overview"),

	path('contacts/', views.contactList, name = "contacts"),
	path('contacts/<str:pk>/', views.contactDetail, name = "contacts_crud"),

	path('persons/', views.contactList, name = "persons"),
	path('persons/<str:pk>/', views.contactDetail, name = "persons_crud"),

	path('addresses/', views.getAddressEntry, name = "addresses"),
	


]
