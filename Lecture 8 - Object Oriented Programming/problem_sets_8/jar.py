class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        # self.capacity
        # self.cookies
        self._capacity = capacity
        # self._cookies
        self._size = 0


    def __str__(self):
        return self._size * "🍪"


    def deposit(self, n):
        if n > self.capacity:
            raise ValueError("Can't deposit more cookies than jar capacity!")
        if self._size + n > self.capacity:
            raise ValueError("Can't deposit more cookies than jar capacity!")
        
        self._size += n


    def withdraw(self, n):
        if self._size < n:
            raise ValueError("Can't withdraw more cookies than you have, greedy fingers!")
        
        self._size -= n
    
    
    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
        

def main():
    jar = Jar()
    jar.deposit(2)
    print(jar)
    jar.withdraw(1)
    print(jar)


if __name__ == "__main__":
    main()

