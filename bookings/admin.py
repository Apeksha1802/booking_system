from django.contrib import admin
from .models import Coupon, Booking

# Register your models here.

admin.site.register(Coupon)

admin.site.register(Booking)