from django.contrib import admin

# Register your models here.
from .models import Booking
from .models import Course
from .models import Contact

admin.site.register(Booking)
admin.site.register(Course)
admin.site.register(Contact)