"""
Purified fields for Django forms
"""

from django import forms

from purifier import HTMLPurifier


class PurifyedCharField(forms.CharField):
    """
    Extendable django.forms.CharField
    Add named argument `white_list` - dict of allowed tags and attributes
    """
       
    def __init__(self, white_list={}, *args, **kwargs):
        self._white_list = white_list
        super(PurifyedCharField, self).__init__(*args, **kwargs)

    def clean(self, value):
        value = super(PurifyedCharField, self).clean(value)
        purifier = HTMLPurifier(self._white_list)
        return purifier.feed(value)
