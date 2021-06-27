from django.db import models


class ProfileModel(models.Model):
    budget = models.IntegerField()
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
