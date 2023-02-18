from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class CarData(models.Model):
    vin = models.CharField(max_length=200)
    year = models.CharField(max_length=500,db_index=True)
    make=models.CharField(max_length=500,db_index=True)
    model=models.CharField(max_length=500,db_index=True)
    trim = models.CharField(max_length=500)
    dealer_name = models.CharField(max_length=500)
    dealer_street = models.CharField(max_length=500)
    dealer_city = models.CharField(max_length=500)
    dealer_state = models.CharField(max_length=500)
    dealer_zip = models.CharField(max_length=500)
    listing_price = models.CharField(max_length=500)
    listing_mileage = models.CharField(max_length=500)
    used = models.CharField(max_length=500)
    certified = models.CharField(max_length=500)
    style = models.CharField(max_length=500)
    driven_wheels = models.CharField(max_length=500)
    engine = models.CharField(max_length=500)
    fuel_type = models.CharField(max_length=500)
    exterior_color = models.CharField(max_length=500)
    interior_color = models.CharField(max_length=500)
    seller_website = models.CharField(max_length=500)
    first_seen_date = models.CharField(max_length=500)
    last_seen_date = models.CharField(max_length=500)
    dealer_vdp_last_seen_date = models.CharField(max_length=500)
    listing_status = models.CharField(max_length=500)
    class Meta:
        managed = True
        db_table = 'car_data'