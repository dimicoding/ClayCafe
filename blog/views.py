from django.shortcuts import render
from django.views.generic import ListView
from .models import Blog, Comment
# Create your views here.

def blog(request):

    return render(request,"blog/blog.html", {})


class HomeView(ListView):
    """
    Accessible from "blog" navbar, displays all blog posts
    """

    model = Blog
    template_name = "blog/blog.html"
    ordering = ["created_blog"]

    # Dropdown menu list
    # def get_context_data(self, *args, **kwargs):
    #     cat_list = Category.objects.all()
    #     context = super(HomeView, self).get_context_data(*args, **kwargs)
    #     context["cat_list"] = cat_list
    #     return context
