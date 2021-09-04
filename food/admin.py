from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import OrderInstance, BusinessObject

# Register your models here.
admin.site.register(Permission)
admin.site.register(OrderInstance)
admin.site.register(BusinessObject)