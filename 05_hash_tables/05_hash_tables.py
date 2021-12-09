

hash(1)
hash(10)
hash(10.01)
hash(-10.01)

hash(0.1) == hash(230584300921369408)

''' hash any object! '''

hash('Hello world')

class Car:
    color = 'red'
    speed = 160

c1 = Car()
hash(c1)

''' A hash table is a data structure that allows you to store a collection of key-value pairs. '''

class Hashtable:
    def __init__(self, elements):
        self.bucket_size = len(elements)
        self.buckets = [[] for i in range(self.bucket_size)]
        self._assign_buckets(elements)

    def _assign_buckets(self, elements):
        for key, value in elements:
            hashed_value = hash(key)
            index = hashed_value % self.bucket_size
            self.buckets[index].append((key, value))

    def get_value(self, input_key):
        hashed_value = hash(input_key)
        index = hashed_value % self.bucket_size
        bucket = self.buckets[index]
        for key, value in bucket:
            if key == input_key:
                return(value)
        return None

    def __str__(self):
        return str(self.buckets)

capitals = [
    ('France', 'Paris'),
    ('United States', 'Washington D.C.'),
    ('Italy', 'Rome'),
    ('Canada', 'Ottawa')
]

hashtable = Hashtable(capitals)
print(hashtable)
print(f"The capital of Italy is {hashtable.get_value('Italy')}")
