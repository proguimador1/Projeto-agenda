from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone',)
    ordering = '-id',
    search_fields = 'first_name', 'last_name', 'phone',
    list_per_page = 15
    list_max_show_all = 150
    list_editable = 'first_name', 'last_name',
    list_display_links = 'id',

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',