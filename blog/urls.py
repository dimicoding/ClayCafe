from django.urls import path
from .views import HomeView, BlogDetailView, BlogLike


urlpatterns = [
    path("", HomeView.as_view(), name="blog"),
    path("post/<int:pk>", BlogDetailView.as_view(), name="the_blog"),
    path("like/<int:pk>", BlogLike, name="blog_like"),
]
