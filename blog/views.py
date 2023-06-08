from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .models import Blog, Comment
from .forms import CommentForm
from django.contrib import messages
# Create your views here.


def blog(request):

    return render(request, "blog/blog.html", {})


class HomeView(ListView):
    """
    Accessible from "blog" navbar, displays all blog posts
    """

    model = Blog
    template_name = "blog/blog.html"
    ordering = ["created_blog"]


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog-detail.html"

    def get_context_data(self, *args, **kwargs):
        """Dropdown menu list"""
        context = super(BlogDetailView, self).get_context_data(*args, **kwargs)

        """ Indentify the specific post place"""
        place = get_object_or_404(Blog, id=self.kwargs["pk"])
        number_likes = place.number_likes()

        comments = Comment.objects.filter(approved=True).order_by("created_on")

        if self.request.user.is_authenticated:
            context["comment_form"] = CommentForm(instance=self.request.user)

        liked = False
        if place.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["number_likes"] = number_likes
        context["liked"] = liked
        context["comments"] = comments
        return context

    def post(self, request, *args, **kwargs):
        new_comment = Comment(
            body=request.POST.get("body"),
            name=self.request.user,
            post=self.get_object(),
        )
        new_comment.save()
        messages.success(
            request,
            "Your comment was successfully submitted! Awaiting approval."
        )
        return self.get(self, request, *args, **kwargs)


def BlogLike(request, pk):
    """Defining Like View"""

    post = get_object_or_404(Blog, id=request.POST.get("blog_id"))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse("the_blog", args=[str(pk)]))
