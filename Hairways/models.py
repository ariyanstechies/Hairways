from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    nickname= models.CharField(max_length=30,null=True,blank=True)


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nickname=models.CharField(max_length=30)
    email= models.CharField(max_length=30, default='myemail@gmail.com')


class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    ownerName = models.CharField(max_length=30)
    email = models.TextField(max_length=150)
    phone = models.PositiveIntegerField()
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.ownerName


class Salons(models.Model):
    saloonName = models.CharField(max_length=20)
    description = models.TextField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    Owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='my_salons')
    likes = models.IntegerField(null=True, blank=True)
    views = models.IntegerField(null=True, blank=True)
    status = models.BooleanField(default=True)
    shares = models.IntegerField(null=True, blank=True)
    paybill = models.TextField(null=True, blank=True, max_length=12)
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.saloonName

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


class Services(models.Model):
    salons = models.ForeignKey(Salons, on_delete=models.CASCADE, related_name='services')
    serviceName = models.CharField(max_length=100)
    serviceCost = models.CharField(max_length=50)
    serviceDuration = models.CharField(max_length=20)
    serviceBookings = models.IntegerField()
    svailability = models.BooleanField(default=True)

    def __str__(self):
        return self.serviceName

class Appointments(models.Model):
    client= models.ForeignKey(User, on_delete=models.CASCADE, default=1,related_name='my_appointments')
    services = models.ManyToManyField(Services)
    salons = models.ForeignKey(Salons, on_delete=models.CASCADE, default=1, related_name='appointments')
    AppointmentsStatus = models.BooleanField()
    date_time = models.DateTimeField()
    totalCost = models.IntegerField()


class Products(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    product_brand = models.CharField(max_length=100)
    salons = models.ForeignKey(Salons, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.product_name




# class Pictures(models.Model):
#     salonId = models.ForeignKey(Salons, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='image/', blank=True, null=True)
#
#     def __str__(self):
#         return self.salonId
#
#     def delete(self, *args, **kwargs):
#         self.image.delete()
#         super().delete(*args, **kwargs)


class Comments(models.Model):
    salon = models.ForeignKey(Salons, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_comments')
    reply = models.TextField(max_length=250)
    created_date = models.DateTimeField(
        default=timezone.now
    )
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.reply
