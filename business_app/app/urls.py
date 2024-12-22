from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_contact/', views.add_contact, name='add_contact'),
    path('upload/', views.upload_file, name='upload_file'),
    path('get_contacts/', views.get_contacts, name='get_contacts'),
]
