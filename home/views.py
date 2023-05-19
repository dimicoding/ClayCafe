from django.shortcuts import render

# Create your views here.

def index(request):
    """View to return index page"""
    return render(request, 'index.html')


def cafemenu(request):
    """View to return cafe menu"""
    return render(request, 'cafe-menu.html')