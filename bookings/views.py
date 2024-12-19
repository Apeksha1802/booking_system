from django.shortcuts import render
from .forms import BookingForm
from .models import Coupon
# Create your views here.

def book_event(request):
  total_price = None
  discount = 0

  if request.method == "POST":
    form = BookingForm(request.POST)
    if form.is_valid():
      event_name = form.cleaned_data['event_name']
      number_of_tickets = form.cleaned_data['number_of_tickets']
      price_per_ticket = form.cleaned_data['price_per_ticket']
      coupon_code = form.cleaned_data['coupon_code']

      # Calculate total price
      total_price = number_of_tickets * price_per_ticket

      # Apply coupon discount if valid
      if coupon_code:
        try:
          coupon = Coupon.objects.get(code=coupon_code)
          discount = (coupon.discount_percentage / 100) * total_price
          total_price -= discount
        except Coupon.DoesNotExist:
          form.add_error('coupon_code', 'Invalid coupon code.')

  else:
    form = BookingForm()

  return render(request, 'booking.html', {'form': form,'total_price': total_price,'discount': discount})