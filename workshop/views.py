from django.shortcuts import render

# Create your views here.

def workshop(request):
    return request(render, 'workshop/workshop.html', {})