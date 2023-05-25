from django.contrib import admin
from .models import Workshop, Booking


class WorkshopAdmin(admin.ModelAdmin):
    """
    Workshop admin panel
    """
    list_display = (
        'title',
        'image',
        'description',
        'start_time',
        'end_time',
        'location',
        'price',
        'places'
    )
    ordering = ('-id',)


class BookingAdmin(admin.ModelAdmin):
    """
    Booking admin panel
    """
    list_display = (
        'created_on',
        'content',
    )



admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Booking, BookingAdmin)