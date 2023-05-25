from django.urls import path
from . import views


urlpatterns = [
    path('', views.workshop, name="workshop"),
]