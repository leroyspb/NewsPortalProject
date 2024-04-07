from django.db import models

# Create your models here

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    text = models.CharField()
    time_in = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()

    def like(self):
        return self.rating + 1


    def dislike(self):
        return self.rating - 1


