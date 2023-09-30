from django.shortcuts import render
from django.http import HttpResponse
from .models import Booking
from . import models
import time 
# Create your views here.
def index(request):
    return render(request , 'index.html')

def appointment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        doctor_id = request.POST.get('doctor')  # Get the doctor's ID
        date = request.POST.get('date')

        # Create a dictionary to map doctor IDs to doctor names
        doctor_names = {
            "1": "Dr.Jessica Robinson(Orthopedics)",
            "2": "Dr.Daniel Clark(Cardiology)",
            "3": "Dr.Joseph Martinez(Neurology)",
            "4": "Dr.Sara Adams(Orthopedics)",
            "5": "Dr.Richard Taylor(Gastroenterology)",
            "6": "Dr.Laura Garcia(Dental Surgery)",
            "7": "Dr.Michael Johnson(Gynecology)",
            "8": "Dr.Christopher White(Cardiology)",
        }

        # Get the doctor's name from the dictionary
        doctor_name = doctor_names.get(doctor_id)

        data = Booking(p_name=name, p_phone=phone, p_email=email, doc_name=doctor_name, booking_date=date)
        data.save()
        time.sleep(2)
        return render(request, 'index.html')

    else:
        return render(request, 'index.html')


