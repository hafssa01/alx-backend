#!/usr/bin/env python3
"""
2. LIFO caching
"""

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.keys_order = []

    def put(self, key, item):
        """Add an item to the cache with LIFO eviction."""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.keys_order.remove(key)
            self.keys_order.append(key)
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                last_key = self.keys_order.pop(-2)
                print(f"DISCARD: {last_key}")
                del self.cache_data[last_key]

    def get(self, key):
        """Retrieve an item from the cache."""
        return self.cache_data.get(key, None)
