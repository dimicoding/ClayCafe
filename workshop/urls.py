from django.urls import path
from . import views


urlpatterns = [
    path('', views.workshop, name="workshop"),
    path('workshop/<int:workshop_id>/',
         views.workshop_book, name="workshop_book"),
    path('workshops/booked/', views.workshops_booked, name="workshops_booked"),

]
