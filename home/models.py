from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.template.defaultfilters import slugify
from phone_field import PhoneField

class tempuser(models.Model):
    name = models.CharField(max_length = 254, )
    phone_no = PhoneField()
    email =  models.EmailField(max_length = 254, blank = True, null = True)

class User(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    nickname = models.CharField(max_length=30, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null = True, blank = True)


class Owner(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    ownerName = models.CharField(max_length=30)
    email = models.CharField(max_length=150)
    phone = models.PositiveIntegerField(default='07000000')
    location = models.CharField(max_length=25, default='Kisumu')
    gender = models.CharField(max_length=150, default='Female')

    def __str__(self):
        return self.ownerName


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Owner.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.owner.save()


class Salon(models.Model):
    name = models.CharField(max_length=100)
    url = models.SlugField()
    description = models.TextField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)
    Owner = models.ForeignKey(
        Owner, on_delete=models.CASCADE, related_name='my_salons')
    views = models.IntegerField(default=0)
    status = models.BooleanField(default=0)
    shares = models.IntegerField(default=0)
    paybill = models.TextField(null=True, blank=True, max_length=12)
    town = models.CharField(max_length=30)
    location_description = models.CharField(max_length = 250, null= True, blank = True)
    likes = models.ManyToManyField(User, related_name='likes')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.url = slugify(self.name)

        super(Salon, self).save(*args, **kwargs)

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    @property
    def total_likes(self):
        """
        Likes for the salon
        :return: Integer: Likes for the salon
        """
        return self.likes.count()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Salon, self).save(*args, **kwargs)


class Services(models.Model):
    salons = models.ForeignKey(
        Salon, on_delete=models.CASCADE, related_name='services')
    serviceName = models.CharField(max_length=100)
    serviceCost = models.CharField(max_length=50)
    serviceDuration = models.CharField(max_length=20)
    serviceBookings = models.IntegerField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.serviceName


class Staff(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    date_started = models.DateTimeField(default=timezone.now)
    salary = models.IntegerField()
    phone = models.IntegerField()
    email = models.CharField(max_length=100)
    favservice = models.CharField(max_length=100, null=True, blank=True)
    favclient = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.firstname


class Client(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True,
        related_name='client')
    Full_Name = models.CharField(max_length=30)
    email = models.CharField(max_length=30, default='myemail@gmail.com')
    phone = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nickname

class Products(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    product_brand = models.CharField(max_length=100)
    salons = models.ForeignKey(
        Salon, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.product_name


class Appointments(models.Model):
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='my_appointments')
    clientphoneNo = models.IntegerField(default='2345966')
    services = models.ManyToManyField(Services, related_name='services')
    products = models.ManyToManyField(Products, related_name='products')
    salons = models.ForeignKey(
        Salon, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateTimeField()
    created_date = models.DateTimeField(default=timezone.now)
    totalCost = models.IntegerField()
    is_accepted = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    is_pending = models.BooleanField(default=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.clientphoneNo)

    def get_absolute_url(self):
        return reverse('appointment_detail', kwargs={'pk': self.pk})




class Comments(models.Model):
    STAR_CHOICES = (
        ('1 Star', '1 star'),
        ('2 Stars', '2 stars'),
        ('3 Stars', '3 stars'),
        ('4 Stars', '4 stars'),
        ('5 Stars', '5 stars'),
    )
    salon = models.ForeignKey(
        Salon, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='my_comments')
    stars = models.CharField(max_length=10, choices=STAR_CHOICES, default='1 star')
    comment = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now
    )

    approved_comment = models.BooleanField(default=False)

    def __str__(self):
        return str(self.author)
    # to be revisited

    def approve(self):
        self.approved_comment = True
        self.save()
