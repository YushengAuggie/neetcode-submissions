class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise Exception("capacity needs to > 0")

        self.capacity = capacity
        self.array = []

    def get(self, i: int) -> int:
        if i < 0 or i > len(self.array):
            raise Exception()
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        self.array[i] = n


    def pushback(self, n: int) -> None:
        if len(self.array) == self.capacity:
            self.resize()
        self.array.append(n)

    def popback(self) -> int:
        return self.array.pop()

    def resize(self) -> None:
        self.capacity *= 2


    def getSize(self) -> int:
        return len(self.array)
        
    
    def getCapacity(self) -> int:
        return self.capacity
