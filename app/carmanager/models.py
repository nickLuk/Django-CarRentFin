from django.db import models
from datetime import datetime


class CarManager(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    position = models.CharField(max_length=50, blank=True)

    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    phone1 = models.CharField(max_length=20, blank=True)
    phone2 = models.CharField(max_length=20, blank=True)
    phone3 = models.CharField(max_length=20, blank=True)
    telegram = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=200)
    # email = models.EmailField()
    
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name
