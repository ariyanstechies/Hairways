from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.template.defaultfilters import slugify


class User(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    nickname = models.CharField(max_length=30, null=True, blank=True)


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
    name = models.CharField(max_length=20)
    url = models.SlugField()
    description = models.TextField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    Owner = models.ForeignKey(
        Owner, on_delete=models.CASCADE, related_name='my_salons')
    views = models.IntegerField(default=0)
    status = models.BooleanField(default=0)
    shares = models.IntegerField(default=0)
    paybill = models.TextField(null=True, blank=True, max_length=12)
    location = models.CharField(max_length=30)
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


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Client.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.client.save()


class Appointments(models.Model):
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='my_appointments')
    clientphoneNo = models.IntegerField(default='2345966')
    services = models.ManyToManyField(Services, related_name='services')
    salons = models.ForeignKey(
        Salon, on_delete=models.CASCADE, related_name='appointments')
    date_time = models.DateTimeField()
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


class Products(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    product_brand = models.CharField(max_length=100)
    salons = models.ForeignKey(
        Salon, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.product_name


class Comments(models.Model):
    salon = models.ForeignKey(
        Salon, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='my_comments')
    reply = models.TextField(max_length=250)
    created_date = models.DateTimeField(
        default=timezone.now
    )
    approved_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.reply
    # to be revisited

    def approve(self):
        self.approved_comment = True
        self.save()
