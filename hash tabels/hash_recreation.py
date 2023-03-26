class HashTable:
    def __init__(self, size):
        self.data = [None]*size
        print(self.data)

    def _hash(self, key):
        hash = 0;
        for i in range(len(key)):
            hash = (hash + int(ord(key[i])) * i) % len(self.data)
        return hash;

    def set(self, key, value):
        address = self._hash(key)
        if not self.data[address]:
            self.data[address] = []
        self.data[address].append([key, value]);
        print(self.data)
        return self.data;

    def get(self, key):
        address = self._hash(key)
        currentBucket = self.data[address]
        if (currentBucket):
            for i in range(len(currentBucket)):
                if currentBucket[i][0] == key:
                    return currentBucket[i][1]
        return None;

myHashTable = HashTable(2);
myHashTable.set('grapes', 10000)
print(myHashTable.get('grapes'))
myHashTable.set('apples', 9)
print(myHashTable.get('apples'))