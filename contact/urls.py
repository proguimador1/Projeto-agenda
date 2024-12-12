from django.urls import path

from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.initial, name='home'),
    path('<int:contact_id>/', views.contact, name='single_contact'),

]