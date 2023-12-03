from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Pizza, Order, UserProfile

admin.site.register(UserProfile)
admin.site.register(Pizza)
admin.site.register(Order)