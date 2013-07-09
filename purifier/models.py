"""
Purified fields for Django ORM
"""

from django.conf import settings
from django.db import models
from django.utils.encoding import smart_unicode

from purifier import HTMLPurifier


class PurifyedCharField(models.CharField):
    """
    Extendable django.db.models.CharField
    Add named argument `white_list` - dict of allowed tags and attributes
    """
    
    def __init__(self, white_list={}, *args, **kwargs):
        self._white_list = white_list
        super(PurifyedCharField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        value = super(PurifyedCharField, self).to_python(value)
        purifier = HTMLPurifier(self._white_list)
        value = purifier.feed(value)
        return smart_unicode(value)


class PurifyedTextField(models.TextField):
    """
    Extendable django.db.models.TextField
    Add named argument `white_list` - dict of allowed tags and attributes
    """
    
    def __init__(self, white_list={}, *args, **kwargs):
        self._white_list = white_list
        super(PurifyedTextField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        value = super(PurifyedTextField, self).to_python(value)
        purifier = HTMLPurifier(self._white_list)
        value = purifier.feed(value)
        return smart_unicode(value)

    def get_prep_value(self, value):
        value = super(PurifyedTextField, self).get_prep_value(value)
        purifier = HTMLPurifier(self._white_list)
        value = purifier.feed(value)
        return value


"""For South compatibility"""
if 'south' in settings.INSTALLED_APPS:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^purifier\.models\.PurifyedCharField"])
    add_introspection_rules([], ["^purifier\.models\.PurifyedTextField"])
