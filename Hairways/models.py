from django.db import models
from django.utils import timezone


class Comments(models.Model):
    CommentId = models.IntegerField()
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now
    )
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class Owners(models.Model):
    OwnerId = models.IntegerField(primary_key=True)
    OwnerName = models.TextField()
    Email = models.TextField()
    Phone = models.IntegerField()
    Password = models.CharField(max_length=50)


class Services(models.Model):
    ServiceId = models.IntegerField(primary_key=True)
    ServiceName = models.TextField()
    ServiceCost = models.TextField()
    ServiceDuration = models.TextField()
    ServiceBookings = models.IntegerField()
    Availability = models.BooleanField(default=True)


class Appoiments(models.Model):
    AppoimentsId = models.CharField(max_length=100, primary_key=True)
    AppoimentsStatus = models.TextField()
    ServicesID = models.ForeignKey(Services, on_delete=models.CASCADE)
    TotalCost = models.IntegerField()
    UserID = models.TextField()


class Salons(models.Model):
    SaloonName = models.TextField()
    Location = models.TextField()
    Description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    OwnerId = models.ForeignKey(Owners, on_delete=models.CASCADE)
    Likes = models.IntegerField()
    CommentsId = models.ForeignKey(Comments, on_delete=models.CASCADE)
    Views = models.IntegerField()
    Status = models.BooleanField(default=True)
    appoinmentsId = models.ForeignKey(Appoiments, on_delete=models.CASCADE)
    ServiceId = models.ForeignKey(Services, on_delete=models.CASCADE)
    Paybill = models.TextField()


class Users(models.Model):
    UserId = models.ForeignKey(Appoiments, on_delete=models.CASCADE)
    UserName = models.TextField()
    Email = models.TextField()
    Phone = models.IntegerField()
    Location = models.TextField()
