from django.shortcuts import render
from .forms import BookingForm
from .models import Coupon
# Create your views here.

def book_event(request):
  form = BookingForm()
  total_price = None
  discount_amount = None
  discount_message = None

  if request.method == 'POST':
    form = BookingForm(request.POST)
    if form.is_valid():
      booking = form.save(commit=False) # Save data to the model instance but don't commit yet
      coupon_code = form.cleaned_data.get('coupon_code')

      # Calculate the total price
      total_price = booking.number_of_tickets * booking.price_per_ticket

      # Validate the coupon code and calculate discount
      if coupon_code:
        try:
          coupon = Coupon.objects.get(code=coupon_code)
          discount_amount = (coupon.discount_percentage / 100) * total_price
          total_price -= discount_amount
          discount_message = f"Coupon applied! {coupon.discount_percentage}% off."
        except Coupon.DoesNotExist:
          discount_message = "Invalid coupon code."
          discount_amount = 0

      # Save the total price and commit the booking
      booking.total_price = total_price
      booking.save()

  return render(request, 'booking.html', {
    'form': form,
    'total_price': total_price,
    'discount_amount': discount_amount,
    'discount_message': discount_message,
  })

