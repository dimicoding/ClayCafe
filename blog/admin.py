from django.contrib import admin
from .models import Blog, Comment

# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """
    Add fields for Blog post in admin panel
    """
    # prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'content', 'featured_image', 'status',)
    search_fields = ['title', 'content']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Add fields for Blog post in admin panel
    """
    # prepopulated_fields = {'slug': ('title',)}
    list_display = ('name', 'body', 'created_on', 'post', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


