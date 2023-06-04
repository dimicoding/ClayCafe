from django.urls import path
from . import views
from .views import HomeView, BlogDetailView, BlogLike


urlpatterns = [
    # path('', views.blog, name="blog"),
    path("", HomeView.as_view(), name="blog"),
    path("recipe/<int:pk>", BlogDetailView.as_view(), name="the_blog"),
    path("like/<int:pk>", BlogLike, name="blog_like"),
]