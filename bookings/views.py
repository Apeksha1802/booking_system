from django.shortcuts import render
from .forms import BookingForm
from .models import Coupon
from django.core.exceptions import ValidationError
# Create your views here.

def book_event(request):
  form = BookingForm()
  total_price = None
  discount_amount = None
  discount_message = None

  if request.method == 'POST':
    form = BookingForm(request.POST)
    if form.is_valid():
      booking = form.save(commit=False) #saving data 
      coupon_code = form.cleaned_data.get('coupon_code')

      #calculating total price
      total_price = booking.number_of_tickets * booking.price_per_ticket

      #validating coupon code and calculating discount
      if coupon_code:
        try:
          coupon = Coupon.objects.get(code=coupon_code)
          discount_amount = (coupon.discount_percentage / 100) * total_price
          total_price -= discount_amount
          discount_message = f"Coupon applied! {coupon.discount_percentage}% off."
        except Coupon.DoesNotExist:
          raise ValidationError("Invalid Coupon Code")

      #save the total price and book the booking
      booking.total_price = total_price
      booking.save()

  return render(request, 'booking.html', {'form': form,'total_price': total_price,'discount_amount': discount_amount,'discount_message': discount_message,})

