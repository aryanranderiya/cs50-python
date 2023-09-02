class Jar:
    def __init__(self, capacity=12):

        if capacity < 0 :
            raise ValueError("Capacity cannnot be less than 0!")

        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if self._size + n > self._capacity :
            raise ValueError("Cannot exceed jar's capacity!")
        self._size +=n

    def withdraw(self, n):
        if self._size < n :
            raise ValueError("Cannot withdraw less than cookies in jar!")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size