from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.utils import timezone
from .models import Workshop, Booking
from .forms import BookingForm


# Create your views here.

def workshop(request):
    workshop_details = Workshop.objects.all()
    for workshop in workshop_details:
        print(workshop.pk)

    context= {
        'workshop_details': workshop_details,
    }

    return render(request, 'workshop/workshop.html', context)


def workshop_book(request, workshop_id):

    workshop = get_object_or_404(Workshop, id=workshop_id)
    workshop_details = Workshop.objects.all()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']

            booking = Booking(workshop_id=workshop, created_on=timezone.now())
            booking.save()

            booking.full_name = full_name
            booking.email = email
            booking.phone_number = phone_number
            booking.save()

            return redirect('workshops_booked')

    else:
        form = BookingForm()

    context = {
        'workshop': workshop,
        'workshop_details': workshop_details,
        'form': form,
    }

    return render(request, 'workshop/workshop-detail.html', context)


def workshops_booked(request):
    return render(request, 'workshop/workshops-booked.html')

