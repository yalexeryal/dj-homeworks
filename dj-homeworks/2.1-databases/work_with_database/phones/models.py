from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    image = models.CharField(max_length=100)
    price = models.IntegerField()
    release_date = models.CharField(max_length=30)
    lte_exists = models.CharField(max_length=30)
    slug = models.SlugField()
