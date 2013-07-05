# -*- coding: utf-8 -*-
"""
HTMLPurifier testing
"""

from purifier import HTMLPurifier



if __name__ == '__main__':
    # for the goals of developing and testing
    import time
    
    start_time = time.clock()
    
    def read_file(name):
        return open(name).read()
    test_whitelist = {
        'p': ['attr-2'],
        'div': ['*'],
        'b': [],
        'i': []
    }
    purifier = HTMLPurifier(test_whitelist)
    #purifier.feed(read_file('../test-data/google.ru.html'))
    #purifier.feed(read_file('../test-data/megatyumen.ru.catalogue.html'))
    #purifier.feed(read_file('../test-data/megatyumen.ru.html'))
    purifier.feed(read_file('../test-data/simple.html'))
    
    print time.clock() - start_time, 's'
