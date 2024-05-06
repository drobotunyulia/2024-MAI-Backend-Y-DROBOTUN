class LRUCache:
    cache = {}

    def __init__(self, capacity: int=10) -> None:
        self.maximum_size = capacity

    def get(self, key: str) -> str:
        value = self.cache.get(key)
        if value:
            del self.cache[key]
            self.cache[key] = value
        else:
            value = ''
        return value

    def set(self, key: str, value: str) -> None:
        if key in self.cache:
            del self.cache[key]
        self.cache[key] = value
        if len(self.cache) > self.maximum_size:
            first_key = next(iter(self.cache))
            del self.cache[first_key]

    def rem(self, key: str) -> None:
        if key in self.cache:
            del self.cache[key]
