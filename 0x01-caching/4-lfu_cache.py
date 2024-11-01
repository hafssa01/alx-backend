#!/usr/bin/env python3
"""
4. LFU caching
"""

from base_caching import BaseCaching
from collections import defaultdict

class LFUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.usage_frequency = defaultdict(int)
        self.keys_order = []

    def put(self, key, item):
        """Add an item to the cache with LFU eviction."""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.keys_order.remove(key)
            self.keys_order.append(key)
            self.cache_data[key] = item
            self.usage_frequency[key] += 1

            if len(self.cache_data) > self.MAX_ITEMS:
                lfu_key = min(self.usage_frequency, key=lambda k: (self.usage_frequency[k], self.keys_order.index(k)))
                print(f"DISCARD: {lfu_key}")
                del self.cache_data[lfu_key]
                del self.usage_frequency[lfu_key]
                self.keys_order.remove(lfu_key)

    def get(self, key):
        """Retrieve an item from the cache and update its frequency."""
        if key in self.cache_data:
            self.usage_frequency[key] += 1
            return self.cache_data[key]
        return None
