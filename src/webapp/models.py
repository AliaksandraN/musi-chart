from django.db import models


class Musician(models.Model):
    author = models.CharField(max_length=100, verbose_name='Author')
    song = models.TextField(max_length=2000, verbose_name='Song', null=True)
    position = models.IntegerField(verbose_name='Position')
