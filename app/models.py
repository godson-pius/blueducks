from django.db import models

# Create your models here.
class Booking(models.Model):
    fullname = models.CharField(max_length=225)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    secondPhone = models.CharField(max_length=20)
    address = models.TextField()
    description = models.FileField(upload_to="booked")
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname

class Course(models.Model):
    courseName = models.CharField(max_length=255)
    courseDesc = models.TextField()
    courseDuration = models.CharField(max_length=20)
    coursePrice = models.CharField(max_length=30)
    startDate = models.DateField()
    schedule = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    requirements = models.TextField()
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.courseName

class Contact(models.Model):
    fullname = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=30)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return super().__str__()