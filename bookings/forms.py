from django import forms
from .models import Booking, Coupon

class BookingForm(forms.Form):
  event_name = forms.CharField(max_length=100, required=True, label="Event Name")
  number_of_tickets = forms.IntegerField(min_value=1, required=True, label="Number of Tickets")
  price_per_ticket = forms.DecimalField(max_digits=8, decimal_places=2, required=True, label="Price per Ticket")
  coupon_code = forms.CharField(max_length=20, required=False, label="Coupon Code")