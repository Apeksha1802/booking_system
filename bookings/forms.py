from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
  coupon_code = forms.CharField(label="Coupon Code", max_length=20, required=False)

  class Meta:
    model = Booking
    fields = ['event_name', 'number_of_tickets', 'price_per_ticket']