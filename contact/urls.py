from django.urls import path

from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.initial, name='home'),
    path('search/', views.search, name='search'),

    #contact CRUD
    path('contact/<int:contact_id>/detail/', views.contact, name='single_contact'),
    path('contact/create/', views.create, name='create'),
    path('contact/<int:contact_id>/update/', views.contact, name='single_contact'),
    path('contact/<int:contact_id>/delete/', views.contact, name='single_contact'),
]