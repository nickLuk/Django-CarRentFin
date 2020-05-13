from django.db import models
from carmanager.models import CarManager
from datetime import datetime


class ArticleList(models.Model):
    photo_article = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    name_article = models.CharField(max_length=200)
    art_date = models.DateTimeField(default=datetime.now, blank=True)
    carmanager = models.ForeignKey(CarManager, on_delete=models.DO_NOTHING)
    text_article = models.TextField(blank=True)
    visible_article = models.BooleanField(default=True)


    def __str__(self):
        return self.name_article


