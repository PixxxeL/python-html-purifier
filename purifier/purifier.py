# -*- coding: utf-8 -*-
"""
"""

from HTMLParser import HTMLParser



class HTMLPurifier(HTMLParser):
    """
    Вырезает теги и атрибуты не в whitelist. Их содержимое - оставляет.
    Формат whitelist:
    {
        'enabled tag name' : ['list of enabled attributes of tag']
    }
    """
    
    DEBUG = False
    ENABLED = True
    
    def handle_starttag(self, tag, attrs):
        """
        """
        if self.DEBUG:
            print 'Encountered a start tag:', tag, attrs
        if tag in self.sanitizelist:
            self.ENABLED = False
            return
        if tag in self.whitelist_keys:
            attrs = self.__attrs_str(tag, attrs)
            attrs = ' ' + attrs if attrs else ''
            self.data.append( u'<%s%s>' % (tag, attrs,) )
        
    def handle_endtag(self, tag):
        """
        """
        if self.DEBUG:
            print 'Encountered an end tag :', tag
        if tag in self.sanitizelist:
            self.ENABLED = True
            return
        if tag in self.whitelist_keys:
            self.data.append(u'</%s>' % tag)
        
    def handle_data(self, data):
        """
        """
        if self.DEBUG:
            print 'Encountered some data  :', data
        if self.ENABLED:
            self.data.append(data)
        
    def feed(self, data):
        """
        """
        HTMLParser.feed(self, data)
        print self.html()
        self.__reset()
    
    def html(self):
        return ''.join(self.data)
        
    def __init__(self, whitelist=None):
        """
        """
        HTMLParser.__init__(self)
        self.__set_whitelist(whitelist)
        self.__reset()
    
    def __reset(self):
        """
        """
        self.data = []
    
    def __set_whitelist(self, whitelist=None):
        """
        """
        self.whitelist = {}
        self.sanitizelist = ['script', 'style']
        self.whitelist.update(whitelist or {})
        self.whitelist_keys = self.whitelist.keys()
    
    def __attrs_str(self, tag, attrs):
        enabled = self.whitelist[tag]
        all = '*' in enabled
        items = []
        for attr in attrs:
            key = attr[0]
            value = attr[1] or ''
            if all or key in enabled:
                items.append( u'%s="%s"' % (key, value,) )
        return u' '.join(items)




if __name__ == '__main__':
    import time
    
    start_time = time.clock()
    
    def read_file(name):
        return open(name).read()
    whitelist = {
        'p': ['attr-2'],
        'div': ['*'],
        'b': [],
        'i': []
    }
    purifier = HTMLPurifier(whitelist)
    #purifier.feed(read_file('../test-data/google.ru.html'))
    #purifier.feed(read_file('../test-data/megatyumen.ru.catalogue.html'))
    purifier.feed(read_file('../test-data/megatyumen.ru.html'))
    #purifier.feed(read_file('../test-data/simple.html'))
    
    print time.clock() - start_time, 's'
