"""
Cuts the tags and attributes from HTML that are not in the whitelist. 
Their content is leaves.

You can use the symbol `*` to allow all tags and/or attributes.

Note that the `script` and `style` tags are removed with content.

The module is based on HTMLParser Class - in the standard Python package. 
No need to pull a dependence, what is also sometimes can be a plus.

Here is purifier.models.PurifyedCharField, purifier.models.PurifyedTextField
for Django ORM and purifier.forms.PurifyedCharField for Django forms
"""

VERSION = (0, 1, 5,)
__version__ = '.'.join(map(str, VERSION))
