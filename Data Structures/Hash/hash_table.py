class HashTable():

    def __init__(self, capacity):
        self._size = capacity
        self._keys = [None] * capacity
        self._values = [None] * capacity


    def put(self, key, data):
        '''
        Add data into hash table.
        :param key:  hash key
        :param data:  value
        :return:
        '''
        index = self._hashFuntion(key)

        # not None -> it is collision
        while self._keys[index] is not None:
            if self._keys[index] == key:
                self._values[index] = data
                return

            # rehashing with open addressing for collision
            index = (index + 1) % self._size

        # insert
        self._keys[index] = key
        self._values[index] = data

    def get(self, key):
        '''
        Get data by key from hash table.
        :param key: key pair
        :return: value of key pair
        '''
        index = self._hashFuntion(key)

        while self._keys[index] is not None:
            if self._keys[index] == key:
                return self._values[index]

            # open addressing for collision try next slot
            index = (index + 1) % self._size

        # if key is not represented in the table.
        return None

    def _hashFuntion(self, key):
        '''
        Hash function generator.
        :param key: key pair
        :return:
        '''
        sum = 0
        for index in range(0, len(key)):
            sum += ord(key[index])

        return sum % self._size


if __name__ == "__main__":

    table = HashTable(10)

    table.put("apple", 10)
    table.put("orange", 20)
    table.put("car", 30)
    table.put("table", 40)

    print(table.get("orange"))
    print(table.get("cavin"))