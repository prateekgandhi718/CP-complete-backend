from django.contrib import admin

# Register your models here.

# Registering the list of factories model:
from .models import Factory, Product
admin.site.register(Factory)
admin.site.register(Product)

