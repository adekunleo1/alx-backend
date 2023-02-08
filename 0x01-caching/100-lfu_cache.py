#!/usr/bin/python3
""" Basic Dictionary for system caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFU cache class that inherits from BaseCaching.
    """

    def __init__(self) -> None:
        """ Initialize class """
        super().__init__()

    def put(self, key, item):
        """ Add key value pair to cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Return value stored cache key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
