from django.contrib import admin
from .models import Owner, Comments, Services, Appointments, Salons, Products, Staff, Client
# Register your models here.
admin.site.register(Owner)
admin.site.register(Comments)
admin.site.register(Services)
admin.site.register(Appointments)
admin.site.register(Salons)
admin.site.register(Products)
admin.site.register(Staff)
admin.site.register(Client)
