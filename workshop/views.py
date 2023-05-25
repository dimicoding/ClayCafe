from django.shortcuts import render
from .models import Workshop, Booking

# Create your views here.

def workshop(request):
    workshop_details = Workshop.objects.all()

    context= {
        'workshop_details': workshop_details,
    }

    return render(request, 'workshop/workshop.html', context)