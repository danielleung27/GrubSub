from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from datetime import date


class SearchForm(forms.Form):
    search_query=forms.CharField(label="", required=True)
