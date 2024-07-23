#!/usr/bin/env python3
""" LFUCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """ LFUCache class
    A caching system that implements the
    LFU (Least Frequently Used) algorithm
    with LRU (Least Recently Used) as a tiebreaker.
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.freq_data = {}

    def put(self, key, item):
        """ Add an item in the cache
        If key or item is None, this method does nothing.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            min_freq = min(self.freq_data.values())
            lfu_keys = [k for k, v in self.freq_data.items() if v == min_freq]

            if len(lfu_keys) == 1:
                lfu_key = lfu_keys[0]
            else:
                lfu_key = next(iter(lfu_keys))

            print("DISCARD: {}".format(lfu_key))
            del self.cache_data[lfu_key]
            del self.freq_data[lfu_key]

        self.cache_data[key] = item
        self.freq_data[key] = self.freq_data.get(key, 0) + 1

    def get(self, key):
        """ Get an item by key
        If key is None or if the key doesn't exist, return None.
        """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            self.freq_data[key] += 1
            return self.cache_data[key]
        return None
