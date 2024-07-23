#!/usr/bin/env python3
""" MRUCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ MRUCache class
    A caching system that implements the
    MRU (Most Recently Used) algorithm.
    Inherits from BaseCaching.
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        If key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.move_to_end(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(last=True)
                print("DISCARD: {}".format(last_key))
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)

    def get(self, key):
        """ Get an item by key
        If key is None or if the key doesn't exist, return None.
        """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
