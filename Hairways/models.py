from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Owners(models.Model):
    ownerId = models.IntegerField(primary_key=True)
    ownerName = models.CharField(max_length=30)
    email = models.TextField(max_length=150)
    phone = models.PositiveIntegerField()
    password = models.CharField(max_length=25)


class Salons(models.Model):
    saloonName = models.CharField(max_length=20)
    location = models.CharField(max_length=30)
    description = models.TextField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    ownerId = models.ForeignKey(Owners, on_delete=models.CASCADE)
    likes = models.IntegerField(null=True, blank=True)
    views = models.IntegerField(null=True, blank=True)
    status = models.BooleanField(default=True)
    paybill = models.TextField(null=True, blank=True, max_length=12)


class Services(models.Model):
    serviceId = models.IntegerField(primary_key=True)
    salons = models.ForeignKey(Salons, on_delete=models.CASCADE)
    serviceName = models.CharField(max_length=100)
    serviceCost = models.CharField(max_length=50)
    serviceDuration = models.CharField(max_length=20)
    serviceBookings = models.IntegerField()
    svailability = models.BooleanField(default=True)


class Users(models.Model):
    username = models.CharField(max_length=25)
    email = models.CharField(max_length=16)
    phone = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    confirm_Password = models.CharField(max_length=16)
    joined_date = models.DateTimeField(
        blank=True, null=True
        )
    location = models.TextField()


class Appointments(models.Model):
    AppointmentsId = models.CharField(max_length=100, primary_key=True)
    services = models.ForeignKey(Services, on_delete=models.CASCADE)
    salons = models.ForeignKey(Salons, on_delete=models.CASCADE)
    AppointmentsStatus = models.BooleanField()
    date_time = models.DateTimeField()
    totalCost = models.IntegerField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE)


class Pictures(models.Model):
    salonId = models.ForeignKey(Salons, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/', blank=True, null=True)

    def __str__(self):
        return self.salonId

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)


class Comments(models.Model):
    commentId = models.IntegerField()
    salons = models.ForeignKey(Salons, on_delete=models.CASCADE)
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    text = models.TextField(max_length=100)
    created_date = models.DateTimeField(
        default=timezone.now
    )
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
