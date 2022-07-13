from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Debt(models.Model):
    name = models.CharField(max_length=100)
    total = models.IntegerField()
    description = models.TextField(max_length=200)
    paymentMin = models.DecimalField(max_digits= 7 , decimal_places= 2, default=0)
    interest = models.DecimalField(max_digits= 5 , decimal_places= 3, default=0)
    startDate = models.DateField(default=date.today)
    paymentDay = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name