class Jar:
    def __init__(self, capacity = 12):
        self.capacity = capacity
        self.size = 0             # Empty jar

    def __str__(self):
        return "🍪"*self.size

    def deposit(self, m):
        if self.size + m > self.capacity:
            raise ValueError("Beyond jar's capacity")
        self.size += m

    def withdraw(self, m):
        if m > self.size:
            raise ValueError("Not that many cookies available")
        self.size -= m

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, m):
        self._size = m



#------ Testing --------
if __name__ == "__main__":
    jar = Jar(10)
    jar.deposit(3)
    print(jar)
    print(jar.capacity)
    print(jar.size)

