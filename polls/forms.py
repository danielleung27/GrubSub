from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from datetime import date


class SearchForm(forms.Form):
    search_query=forms.CharField(label="", required=True)

    def clean(self):
        cleaned_data = super(SearchForm, self).clean()
        search_query = cleaned_data.get("search_query")

        if (not search_query.isalpha()):
            raise forms.ValidationError("Invalid food query")

        return cleaned_data