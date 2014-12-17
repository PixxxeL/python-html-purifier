# -*- coding: utf-8 -*-
"""
HTMLPurifier testing
This is not doc- or unit tests.
"""

import time
from purifier import HTMLPurifier

try:
    import bleach
except ImportError:
    bleach = None


CODING = 'utf-8'

test_data_files = [
    '../test-data/google.ru.html',
    '../test-data/megatyumen.ru.catalogue.html',
    '../test-data/megatyumen.ru.html',
    '../test-data/simple.html',
    '../test-data/quoted_test.html',
    '../test-data/custom-1.html',
]

HTMLPurifier_test_whitelist = {
    'p': ['attr-2'],
    'div': ['*'],
    'b': [],
    'i': []
    #'br': []
    #'*': ['*'],
}

bleach_test_whitelist = {
    'tags'  : ['p', 'div', 'b', 'i'],
    'attrs' : ['attr-2']
}

def read_file(name):
    return open(name, 'rb').read().decode(CODING)

def HTMLPurifier_test(index=3, whitelist=HTMLPurifier_test_whitelist):
    purifier = HTMLPurifier(whitelist)
    data = read_file(test_data_files[index])
    return purifier.feed(data)

def bleach_test(index=3):
    if bleach:
        return bleach.clean(
            read_file(test_data_files[index]), 
            tags = bleach_test_whitelist['tags'],
            attributes = bleach_test_whitelist['attrs'],
            strip = False
        )

if __name__ == '__main__':
    start_time = time.clock()
    index = 1
    print( HTMLPurifier_test(index) )
    #print HTMLPurifier_test(index, whitelist=None)
    #print bleach_test(index)
    print( '{0} s'.format(time.clock() - start_time) )
