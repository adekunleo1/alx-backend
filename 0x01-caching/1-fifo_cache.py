#!/usr/bin/env python3
"""
First In First Out Caching module
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    represents object storage to retrieve items from a dictionary when limit is reached
    """

    def __init__(self):
        """
        Initialize cache
        """
        super().__init__()
        self.key_indexes = []

    def put(self, key, item):
        """
        assign the item value key to the dictionary self.cache_data
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                item_discarded = self.key_indexes.pop(0)
                del self.cache_data[item_discarded]
                print("DISCARD:", item_discarded)

            self.cache_data[key] = item
            self.key_indexes.append(key)

    def get(self, key):
        """
        returns the key linked self.cache_data
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
