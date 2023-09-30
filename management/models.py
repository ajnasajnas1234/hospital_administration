from django.db import models

# Create your models here.






class Booking(models.Model):
    p_name = models.CharField(max_length=500)
    p_phone = models.IntegerField()
    p_email = models.EmailField()
    doc_name = models.CharField(max_length=500)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)

    def __str__(self):
         return self.p_name
    
