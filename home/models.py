from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone
from phone_field import PhoneField


class tempuser(models.Model):
    name = models.CharField(max_length=254, )
    phone_no = PhoneField()
    email = models.EmailField(max_length=254, blank=True, null=True)


class User(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    nickname = models.CharField(max_length=30, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)


class Owner(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=150)
    phone = models.PositiveIntegerField(default='07000000')
    location = models.CharField(max_length=25, default='Kisumu')
    gender = models.CharField(max_length=150, default='Female')

    def __str__(self):
        return self.name


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Owner.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.owner.save()


class Salon(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)
    owner = models.OneToOneField(Owner,
                                 on_delete=models.CASCADE,
                                 related_name='my_salons')
    rating = models.FloatField(default=0.0)
    status = models.BooleanField(default=0)
    shares = models.IntegerField(default=0)
    paybill = models.IntegerField(null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    town = models.CharField(max_length=30)
    location_description = models.CharField(max_length=250,
                                            null=True,
                                            blank=True)
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6,  null=True, blank=True)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True)
    card_img = models.CharField(max_length=250, blank=True, null=True)
    cover_img = models.CharField(max_length=250, blank=True, null=True)
    promo_img = models.CharField(max_length=250, blank=True, null=True)

    def pending_appointments(self):
        return self.appointments.filter(status="Pending")

    def completed_appointments(self):
        return self.appointments.filter(status="Completed")

    def approved_reviews(self):
        return self.reviews.filter(approved_review=True)

    def pending_reviews(self):
        return self.reviews.filter(approved_review=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Salon, self).save(*args, **kwargs)

    class Meta:

        verbose_name = _('Salon')
        verbose_name_plural = _('Salons')

    def __str__(self):
        return self.name


class Package(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()

    class Meta:

        verbose_name = _('Package')
        verbose_name_plural = _('Packages')

    def __str__(self):
        return self.name


class PackageDetail(models.Model):
    package = models.ForeignKey(
        Package, on_delete=models.CASCADE, related_name='package_details')
    detail = models.CharField(max_length=100)

    class Meta:

        verbose_name = _('PackageDetail')
        verbose_name_plural = _('PackageDetails')

    def __str__(self):
        return str(self.package)


class MpesaTransaction(models.Model):
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    mpesa_receipt_number = models.CharField(max_length=100)
    transaction_date = models.DateTimeField(blank=True, null=True)
    phone_number = models.CharField(max_length=100)
    is_successfull = models.BooleanField(default=False)
    failure_cause = models.TextField(max_length=200)

    class Meta:

        verbose_name = _('MpesaTransaction')
        verbose_name_plural = _('MpesaTransactions')

    def __str__(self):
        return self.MpesaReceiptNumber


class Services(models.Model):
    service_identifier = models.CharField(max_length=200)
    salon = models.ForeignKey(Salon,
                              on_delete=models.CASCADE,
                              related_name='services')
    name = models.CharField(max_length=100)
    cost = models.IntegerField()
    duration = models.IntegerField()
    availability = models.BooleanField(default=True)

    def save(self):
        if not self.id:
            super(Services, self).save()
            self.service_identifier = ('SN' + str(self.id))
        super(Services, self).save()

    class Meta:

        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    brand = models.CharField(max_length=100)
    product_identifier = models.CharField(max_length=200)
    salon = models.ForeignKey(Salon,
                              on_delete=models.CASCADE,
                              related_name='products')

    def save(self):
        if not self.id:
            super(Products, self).save()
            self.product_identifier = ('PN' + str(self.id))
        super(Products, self).save()

    class Meta:

        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name


class Staff(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True,
                                related_name='staff')
    salon = models.ForeignKey(Salon,
                              on_delete=models.CASCADE,
                              related_name='staffs')
    firstname = models.CharField(max_length=100, null=True, blank=True)
    lastname = models.CharField(max_length=100, null=True, blank=True)
    date_started = models.DateField(default=timezone.now)
    salary = models.IntegerField(null=True, blank=True)
    job_description = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.firstname


class Client(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True,
                                related_name='client')
    Full_Name = models.CharField(max_length=30)
    email = models.CharField(max_length=30, default='myemail@gmail.com')
    phone = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nickname


class Appointments(models.Model):
    STATUS_CHOICES = (('Accepted', 'Accepted'), ('Rejected', 'Rejected'),
                      ('Pending', 'Pending'), ('Completed', 'Completed'))
    client = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='my_appointments')
    clientphoneNo = models.IntegerField(default='2345966')
    services = models.ManyToManyField(Services, related_name='servicess')
    products = models.ManyToManyField(Products, related_name='productss')
    salon = models.ForeignKey(Salon,
                              on_delete=models.CASCADE,
                              related_name='appointments')

    appointment_date = models.DateTimeField()
    created_date = models.DateTimeField(default=timezone.now)
    totalCost = models.IntegerField()
    status = models.CharField(max_length=50,
                              choices=STATUS_CHOICES,
                              default='Pending')

    def get_absolute_url(self):
        return reverse('appointment_detail', kwargs={'pk': self.pk})

    class Meta:

        verbose_name = _('Appointment')
        verbose_name_plural = _('Appointments')

    def __str__(self):
        return f'{str(self.id)} {str(self.created_date)}'


class AppointmentPayment(models.Model):
    PAYMENT_METHODS = (('M-pesa', 'M-pesa'), ('Cash', 'Cash'))
    appointment = models.ForeignKey(Appointments,
                                    on_delete=models.CASCADE,
                                    related_name='appointment_payments')
    total_amount = models.IntegerField()
    payment_method = models.CharField(max_length=50,
                                      choices=PAYMENT_METHODS,
                                      default='Pending')

    class Meta:

        verbose_name = _('AppointmentPayment')
        verbose_name_plural = _('AppointmentPayments')

    def __str__(self):
        return str(self.appointment)


class Reviews(models.Model):
    STAR_CHOICES = (
        ('1 Star', '1 star'),
        ('2 Stars', '2 stars'),
        ('3 Stars', '3 stars'),
        ('4 Stars', '4 stars'),
        ('5 Stars', '5 stars'),
    )
    salon = models.ForeignKey(Salon,
                              on_delete=models.CASCADE,
                              related_name='reviews')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='my_reviews')
    stars = models.CharField(max_length=10,
                             choices=STAR_CHOICES,
                             default='1 Star')
    ambience_rating = models.FloatField()
    cleanliness_rating = models.FloatField()
    staff_rating = models.FloatField()
    message = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    approved_review = models.BooleanField(default=False)

    def approve(self):
        self.approved_review = True
        self.save()

    class Meta:

        verbose_name = _('Review')
        verbose_name_plural = _('Reviews')

    def __str__(self):
        return str(self.author)


class Gallery(models.Model):
    POSITION_CHOICES = (('Cover Image', 'Cover Image'), ('Card Image', 'Card Image'),
                        ('Prome Image', 'Prome Image'))
    salon = models.ForeignKey(Salon,
                              on_delete=models.CASCADE,
                              related_name='gallery')
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    is_selected = models.BooleanField(default=False)
    image_position = models.CharField(
        max_length=60, choices=POSITION_CHOICES)

    class Meta:

        verbose_name = _('Gallery')
        verbose_name_plural = _('Galleries')

    def __str__(self):
        return str(self.id)
