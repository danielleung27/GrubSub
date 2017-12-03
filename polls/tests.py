# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .foother import FoodSearch

from django.test import TestCase

# Create your tests here.

t = FoodSearch()
print(t.similar_entries(3, "burger"))
