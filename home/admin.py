from django.contrib import admin
from home.models import Owner, Reviews, Services, AppointmentPayment
from home.models import Appointments, Salon, Products, Staff, Client, User, SalonSubscription
from home.models import Appointments, Salon, Products, Staff, Gallery, Client, User, SalonSubscription

admin.site.register(Owner)
admin.site.register(Reviews)
admin.site.register(Services)
admin.site.register(Appointments)
admin.site.register(Salon)
admin.site.register(Products)
admin.site.register(Staff)
admin.site.register(Client)
admin.site.register(User)
admin.site.register(SalonSubscription)
admin.site.register(AppointmentPayment)
admin.site.register(Gallery)
