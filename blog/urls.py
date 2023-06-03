from django.urls import path
from . import views
from .views import HomeView


urlpatterns = [
    # path('', views.blog, name="blog"),
    path("", HomeView.as_view(), name="blog"),
]