from django.shortcuts import render
from .forms import ContactForm

# Create your views here.

def index(request):
    """View to return index page"""
    return render(request, 'index.html')

def contact(request):
    """View to return index page"""

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            matter = form.cleaned_data["matter"]
            message = form.cleaned_data["message"]

            subject = "Client Contant Form"
            body = f"Name:{name}\nMatter:{matter}\nEmail:{email}\n\nMessage:\n{message}"

            send_mail(
                subject,
                body,
                email,
                matter,
                ["claycafeartisanal@gmail.com"],
                fail_silently=False,
            )
            return render(request, "contact.html", {"name": name})
    else:
        form = ContactForm()
    return render(
        request,
        "contact.html", {"form": form})