from django.db import models

# Create your models here.
class Author(models.Model):
    full_name = models.CharField(max_length=255)
    age = models.IntegerField(default='Не указан')
    born_country = models.CharField(max_length=255, default="Не указано")
    author = models.OneToOneField('User')
    rating_author = models.IntegerField(default=0)
    def update_rating(self):
        return self.rating_author + 1