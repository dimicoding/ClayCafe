from django import forms
from django.forms import ModelForm

enquiry_choices = [
    ('products', 'Products'),
    ('blog', 'Blog'),
    ('collaboration', 'Collaboration'),
    ('workshops', 'Workshops'),
    ('cafe', 'Cafe'),
    ('other', 'Other'),
]

class ContactForm(forms.Form):
    name = forms.CharField(
        required=True, widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Name:"})
    )
    email = forms.EmailField(
        required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Email:"})
    )
    matter = forms.ChoiceField(
        required=True, choices=enquiry_choices, widget=forms.Select(attrs={"class": "form-control",}))
    
    message = forms.CharField(
        required=True, widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Message:"})
    )