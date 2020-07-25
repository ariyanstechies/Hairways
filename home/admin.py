from django.contrib import admin
from home.models import Vendor, Review, Service, AppointmentPayment, Package, MpesaTransaction, PackageDetail
from home.models import Appointment, Salon, Product, Gallery, Customer, User, Location

admin.site.register(Vendor)
admin.site.register(Review)
admin.site.register(Service)
admin.site.register(Appointment)
admin.site.register(Salon)
admin.site.register(Location)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(User)
admin.site.register(AppointmentPayment)
admin.site.register(Gallery)
admin.site.register(Package)
admin.site.register(MpesaTransaction)
admin.site.register(PackageDetail)
