#!/usr/bin/python3
""" LIFO Caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ A basic cache that inherits from class BaseCaching
    """

    def put(self, key, item):
        """ Add key/value pair to cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Return the value stored in cache key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
