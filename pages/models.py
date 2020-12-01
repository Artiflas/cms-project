from django.db import models

# Create your models here.


class Team(models.Model):
    vorname = models.CharField(max_length=255)
    familienname = models.CharField(max_length=255)
    beruf = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    google_plus_link = models.URLField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vorname
