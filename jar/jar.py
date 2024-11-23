class Jar:
    def __init__(self, capacity=12):
        if capacity <= 0:
            raise ValueError('Capacity must not be a negative number')
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        cookies = '🍪'
        n_cookies = ''
        for n in range(self._size):
            n_cookies += cookies
        return n_cookies

    def deposit(self, deposit):
        if deposit > self.capacity or deposit < 0 or deposit > self.remaining_capacity:
            raise ValueError('Deposit exceeds capacity or is a negative number')
        elif deposit and not deposit < 0:
            self._size += deposit

    def withdraw(self, withdraw):
        if withdraw < 0 or withdraw > self._size:
              raise ValueError('Withdraw is bigger than the amount of cookies')
        elif withdraw and not withdraw < 0:
             self._size -= withdraw

    @property
    def capacity(self):
        return self._capacity

    @property
    def capacity(self):
        return self._capacity

    @property
    def remaining_capacity(self):
        return self.capacity - self._size

    @property
    def size(self):
        return self._size

