


class HashTable:
    # Initialize the constructor with the size of 10
    def __init__(self, size=10):
        self.hashtable = []
        for i in range(size):
            self.hashtable.append([])

    # Basic hash key that utilize the modulo of package ID as key
    # O(1)
    # Private
    def _hashkey_generator_(self, key):
        hashkey = key % len(self.hashtable)
        return hashkey

    # Insert a new item into the hash table - O(1)
    def add(self, key, item):  # does both insert and update

        bucket_list = self.hashtable[self._hashkey_generator_(key)]
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                kv[1] = item
                return True
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Search for an item by key, and return the item - O(log n)
    def get(self, key):

        bucket_list = self.hashtable[self._hashkey_generator_(key)]
        # search for the key in the bucket list
        for kv in bucket_list:
          #print (key_value)
          if kv[0] == key:
            return kv[1] # value
        return None

