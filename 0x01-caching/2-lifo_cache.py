#!/usr/bin/env python3
""" LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class
    A caching system that implements the LIFO algorithm.
    Inherits from BaseCaching.
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache
        If key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = self.order.pop()
                del self.cache_data[last_key]
                print("DISCARD: {}".format(last_key))
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Get an item by key
        If key is None or if the key doesn't exist, return None.
        """
        return self.cache_data.get(key, None)
