from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from io import BytesIO
from django.core.files.storage import default_storage
from PIL import Image


class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    phone_number = models.CharField(_("Phone Number"), max_length=16)


class Vendor(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True)

    def __str__(self):
        return self.user.first_name


class Customer(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True,
                                related_name='client')

    def __str__(self):
        return self.user.first_name


class Profile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='profile')
    image = models.ImageField(default='avatar/default.jpg',
                              upload_to='avatar/')

    def __str__(self):
        return f'{self.user.get_full_name()} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        memfile = BytesIO()

        img = Image.open(self.image)
        # To resize the profile image
        if img.height > 400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size, Image.ANTIALIAS)
            img.save(memfile, 'JPEG', quality=95)
            default_storage.save(self.image.name, memfile)
            memfile.close()
            img.close()


class Location(models.Model):
    city = models.CharField(max_length=30)
    description = models.CharField(max_length=250,
                                   null=True,
                                   blank=True)
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6,  null=True, blank=True)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True)

    def __str__(self):
        return f'{self.city}, {self.description}'


class Gallery(models.Model):
    TYPES = (('Cover Image', 'Cover Image'),
             ('Card Image', 'Card Image'),
             ('Promo Image', 'Promo Image'))
    image = models.FileField(_("Image"),
                             upload_to='images/', null=True, blank=True)
    is_selected = models.BooleanField(default=False)
    image_type = models.CharField(max_length=60,
                                  choices=TYPES, default="Cover Image")

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'

    def __str__(self):
        return self.get_image_type_display()


class Salon(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)
    vendor = models.OneToOneField(Vendor,
                                  on_delete=models.CASCADE,
                                  related_name='salons')
    paybill = models.IntegerField(null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    location = models.OneToOneField(Location,
                                    on_delete=models.CASCADE,
                                    related_name='location')

    gallery = models.ForeignKey(Gallery,
                                on_delete=models.CASCADE,
                                related_name='gallery', blank=True, null=True)

    def pending_appointments(self):
        return self.appointments.filter(status="Pending")

    def completed_appointments(self):
        return self.appointments.filter(status="Completed")

    def approved_reviews(self):
        return self.reviews.filter(approved=True)

    def pending_reviews(self):
        return self.reviews.filter(approved=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Salon, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Salon'
        verbose_name_plural = 'Salons'

    def __str__(self):
        return self.name


class Service(models.Model):
    salon = models.ForeignKey(Salon,
                              on_delete=models.CASCADE,
                              related_name='services')
    identifier = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    cost = models.IntegerField()
    duration = models.IntegerField()
    availability = models.BooleanField(default=True)

    def save(self):
        if not self.id:
            super(Services, self).save()
            self.identifier = ('SV' + str(self.id))
        super(Services, self).save()

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    brand = models.CharField(max_length=100)
    identifier = models.CharField(max_length=200)
    salon = models.ForeignKey(Salon,
                              on_delete=models.CASCADE,
                              related_name='products')

    def save(self):
        if not self.id:
            super(Product, self).save()
            self.identifier = ('PD' + str(self.id))
        super(Product, self).save()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


class Appointment(models.Model):
    customer = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name='appointments')
    services = models.ManyToManyField(Service, related_name='services')
    products = models.ManyToManyField(Product, related_name='products')
    salon = models.ForeignKey(Salon,
                              on_delete=models.CASCADE,
                              related_name='appointments')

    appointment_date = models.DateTimeField()
    created_date = models.DateTimeField(default=timezone.now)
    totalCost = models.IntegerField()
    STATUS_CHOICES = (('Accepted', 'Accepted'), ('Declined', 'Declined'),
                      ('Pending', 'Pending'), ('Completed', 'Completed'))
    status = models.CharField(max_length=50,
                              choices=STATUS_CHOICES,
                              default='Pending')

    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'

    def __str__(self):
        return f'{str(self.id)} {str(self.created_date)}'


class AppointmentPayment(models.Model):
    appointment = models.ForeignKey(Appointment,
                                    on_delete=models.CASCADE,
                                    related_name='appointment_payments')
    total_amount = models.IntegerField()
    PAYMENT_METHODS = (('M-pesa', 'M-pesa'),
                       ('Cash', 'Cash'))
    payment_method = models.CharField(max_length=50,
                                      choices=PAYMENT_METHODS,
                                      default='Pending')

    class Meta:
        verbose_name = 'AppointmentPayment'
        verbose_name_plural = 'AppointmentPayments'

    def __str__(self):
        return str(self.appointment)


class Review(models.Model):
    salon = models.ForeignKey(Salon,
                              on_delete=models.CASCADE,
                              related_name='reviews')
    customer = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name='my_reviews')

    STAR_CHOICES = (
        ('1 Star', '1 star'),
        ('2 Stars', '2 stars'),
        ('3 Stars', '3 stars'),
        ('4 Stars', '4 stars'),
        ('5 Stars', '5 stars'),
    )
    stars = models.CharField(max_length=10,
                             choices=STAR_CHOICES,
                             default='1 Star')
    content = models.TextField(_('Content'))

    ambience_rating = models.FloatField()
    cleanliness_rating = models.FloatField()
    staff_rating = models.FloatField()
    created_date = models.DateTimeField(default=timezone.now)

    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved = True
        self.save()

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return str(self.author)


class Package(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()

    class Meta:
        verbose_name = 'Package'
        verbose_name_plural = 'Packages'

    def __str__(self):
        return self.name


class PackageDetail(models.Model):
    package = models.ForeignKey(Package,
                                on_delete=models.CASCADE,
                                related_name='package_details')
    detail = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'PackageDetail'
        verbose_name_plural = 'PackageDetails'

    def __str__(self):
        return str(self.package.name)


class MpesaTransaction(models.Model):
    # TODO refactor
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    mpesa_receipt_number = models.CharField(max_length=100)
    transaction_date = models.DateTimeField(blank=True, null=True)
    phone_number = models.CharField(max_length=100)
    is_successfull = models.BooleanField(default=False)
    failure_cause = models.TextField(max_length=200)

    class Meta:
        verbose_name = 'MpesaTransaction'
        verbose_name_plural = 'MpesaTransactions'

    def __str__(self):
        return self.mpesa_receipt_number
