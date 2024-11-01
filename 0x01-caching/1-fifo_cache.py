#!/usr/bin/env python3
"""
1. FIFO caching
"""
from base_caching import BaseCaching
from collections import OrderedDict

class FIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache with FIFO eviction."""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                print(f"DISCARD: {first_key}")
                self.cache_data.pop(first_key)

    def get(self, key):
        """Retrieve an item from the cache."""
        return self.cache_data.get(key, None)
