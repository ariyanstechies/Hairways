from django.contrib import admin
from home.models import Owner, Reviews, Services, AppointmentPayment, Package, MpesaTransaction, PackageDetail
from home.models import Appointments, Salon, Products, Staff, Gallery, Client, User

admin.site.register(Owner)
admin.site.register(Reviews)
admin.site.register(Services)
admin.site.register(Appointments)
admin.site.register(Salon)
admin.site.register(Products)
admin.site.register(Staff)
admin.site.register(Client)
admin.site.register(User)
admin.site.register(AppointmentPayment)
admin.site.register(Gallery)
admin.site.register(Package)
admin.site.register(MpesaTransaction)
admin.site.register(PackageDetail)
