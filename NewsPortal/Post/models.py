from django.db import models
from .resources import PAPER
# Create your models here.
class News(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    article_or_news = models.CharField(max_length=2, choices=PAPER)
    time_in = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField('Category', through='PostCategory')
    name = models.CharField(max_length=255)
    text = models.CharField(max_length=1000)
    rating = models.FloatField(default=0.0)

