from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))


class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_blog = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True)
    featured_image = models.ImageField()
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')

    def number_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.post.title} by {self.name}'