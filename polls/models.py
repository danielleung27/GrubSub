# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from django.utils.encoding import python_2_unicode_compatible

# django model for food listings
class Listing(models.Model):
    id_num = models.IntegerField()
    food_group = models.CharField(max_length=200)
    long_descr = models.CharField(max_length=200)
    short_descr = models.CharField(max_length=200)
    water = models.FloatField()
    energy = models.IntegerField()
    protein = models.FloatField()
    trans_fat = models.FloatField()
    carbohydrate = models.FloatField()
    fiber = models.FloatField()
    sugar = models.FloatField()
    ca = models.FloatField()
    sat_fat = models.FloatField()
    cholesterol = models.FloatField()
    vitamin_b = models.FloatField()
    na = models.FloatField()