Python HTML purifier
====================

About
-----

Cuts the tags and attributes from HTML that are not in the whitelist. 
Their content is leaves. Signature of whitelist:

    {
        'enabled tag name' : ['list of enabled tag's attributes']
    }

You can use the symbol '*' to allow all tags and/or attributes.

Note that the ``script`` and ``style`` tags are removed with content.

The module is based on HTMLParser_. Class - in the standard Python package. 
No need to pull a dependence, what is also sometimes can be a plus.

In my blog_

Basic Use
---------

	>>> purifier = HTMLPurifier({
	    'div': ['*'], # разрешает все атрибуты у тега div
	    'span': ['attr-2'], # разрешает только атрибут attr-2 у тега span
	    # все остальные теги удаляются, но их содержимое остается
	})
	>>> print purifier.feed('&lt;div class="e1" id="e1"&gt;Some &lt;b&gt;HTML&lt;/b&gt; for &lt;span attr-1="1" attr-2="2"&gt;purifying&lt;/span&gt;&lt;/div&gt;')
    <div class="e1" id="e1">Some HTML for <span attr-2="2">purifying</span></div>



.. _HTMLParser: http://docs.python.org/2/library/htmlparser.html
.. _blog: http://pixxxxxel.blogspot.ru/2013/07/html-purifier-python.html