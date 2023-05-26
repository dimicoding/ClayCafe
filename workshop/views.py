from django.shortcuts import render, get_object_or_404
from .models import Workshop, Booking


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

    context = {
        'workshop': workshop,
    }

    return render(request, 'workshop/workshop-detail.html', context)
