from django.shortcuts import render

from .models import Course
from .models import Booking
from .forms import BookingForm

from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'frontend/index.html')

def about(request):
    return render(request, 'frontend/about.html')

def booking(request):
    if (request.method == "POST"):
        fullname = request.POST.get('fullName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        secondPhone = request.POST.get('secondPhone')
        address = request.POST.get('address')
        description = request.FILES.get('description')
        details = request.POST.get('details')
        agreeTerms = request.POST.get('agreeTerms')

        if agreeTerms:
            Booking.objects.create(
                fullname = fullname,
                email = email,
                phone = phone,
                secondPhone = secondPhone,
                address = address,
                description = description,
                details = details,
            )
            messages.success(request, "Saved")
        else:
            print("Accept Terms")

    return render(request, 'frontend/booking.html')

def academy(request):
    courses = Course.objects.all()
    return render(request, 'frontend/academy.html', { 'courses': courses })

def services(request):
    return render(request, 'frontend/services.html')

def contact(request):
    return render(request, 'frontend/contact.html')