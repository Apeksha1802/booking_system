from django.db import models

# Create your models here.

class Booking(models.Model):
  event_name = models.CharField(max_length=100)
  number_of_tickets = models.PositiveIntegerField()
  price_per_ticket = models.DecimalField(max_digits=8, decimal_places=2)
  total_price = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
    return self.event_name

class Coupon(models.Model):
  code = models.CharField(max_length=20, unique=True)
  discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)

  def __str__(self):
    return self.code