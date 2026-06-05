class HashTable:
    def __init__(self, size=50):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return sum(ord(c) for c in key) % self.size

    def insert(self, key, value):
        idx = self._hash(key)

        for item in self.table[idx]:
            if item[0] == key:
                item[1] = value
                return

        self.table[idx].append([key, value])

    def search(self, key):
        idx = self._hash(key)

        for k, v in self.table[idx]:
            if k == key:
                return v

        return None