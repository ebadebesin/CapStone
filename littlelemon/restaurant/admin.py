from django.contrib import admin
from .models import Menu, Booking
# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    Menu = ('id', 'title', 'price', 'inventory')  

class BookingAdmin(admin.ModelAdmin):
    Bookings = ('id', 'name', 'no_of_guests', 'booking_date')

admin.site.register(Menu, MenuAdmin)
admin.site.register(Booking, BookingAdmin)
