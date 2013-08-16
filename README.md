Python HTML purifier
====================

About
-----

Cuts the tags and attributes from HTML that are not in the whitelist. 
Their content is leaves. Signature of whitelist:
```python
{
    'enabled tag name' : ['list of enabled tag\'s attributes']
}
```
You can use the symbol ``*`` to allow all tags and/or attributes.

Note that the ``script`` and ``style`` tags are removed with content.

The module is based on 
[HTMLParser](http://docs.python.org/2/library/htmlparser.html) 
Class - in the standard Python package. 
No need to pull a dependence, what is also sometimes can be a plus.

[Part info in my blog](http://pixxxxxel.blogspot.ru/2013/07/html-purifier-python.html)

[Package on PyPi](https://pypi.python.org/pypi/html-purifier/)

Install
-------

```bash
$ pip install html-purifier
```

Basic Usage
-----------
```python
>>> from purifier.purifier import HTMLPurifier
>>> purifier = HTMLPurifier({
    'div': ['*'], # разрешает все атрибуты у тега div
    'span': ['attr-2'], # разрешает только атрибут attr-2 у тега span
    # все остальные теги удаляются, но их содержимое остается
})
>>> print purifier.feed('<div class="e1" id="e1">Some <b>HTML</b> for <span attr-1="1" attr-2="2">purifying</span></div>')
<div class="e1" id="e1">Some HTML for <span attr-2="2">purifying</span></div>
```

Django Usage
------------

As usual in models and forms.
Here is `purifier.models.PurifyedCharField`, `purifier.models.PurifyedTextField`
for Django ORM and `purifier.forms.PurifyedCharField` for Django forms
