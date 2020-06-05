class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key)

        # key 不存在，未冲突
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            # key 已存在，替换 val
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(hashvalue)
                # 散列冲突，再散列，直到找到空槽或 key
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot)

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data

    def hashfunction(self, key):
        return key % self.size

    def rehash(self, oldhash):
        return (oldhash + 1) % self.size

    def get(self, key):
        # 标记散列值为查找起点
        startslot = self.hashfunction(key)

        data = None
        stop = False
        found = False
        position = startslot
        # 找 key，直到空槽或回到起点
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                # 未找到 key，再散列继续找
                position = self.rehash(position)
                if position == startslot:
                    stop = True             # 回到起点，停

        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)