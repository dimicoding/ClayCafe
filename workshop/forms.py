from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class BookingForm(forms.Form):
    full_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=20, required=True)
    places = forms.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ],
        required=True
    )
