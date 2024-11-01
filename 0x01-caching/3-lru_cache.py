#!/usr/bin/env python3
"""
3. IRU caching
"""

from base_caching import BaseCaching
from collections import OrderedDict

class LRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache with LRU eviction."""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.pop(key)
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                lru_key = next(iter(self.cache_data))
                print(f"DISCARD: {lru_key}")
                self.cache_data.pop(lru_key)

    def get(self, key):
        """Retrieve an item from the cache and mark it as recently used."""
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
