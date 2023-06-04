from django import forms
from django.forms import ModelForm
from .models import Blog, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            "body": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": '"We would love to hear your thoughts..."',
                }
            ),
        }