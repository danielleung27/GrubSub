# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import foother

from django.test import TestCase

# Create your tests here.

t = foother.FoodSearch()
print(t.similar_entries(3, "burger"))
print(t.similar_entries(3, "burger"))
print(t.similar_entries(3, "burger"))
