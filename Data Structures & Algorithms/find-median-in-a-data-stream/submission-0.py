import bisect

class MedianFinder:

    def __init__(self):
        self.list = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.list, num)
        

    def findMedian(self) -> float:
        if len(self.list) % 2 == 0:
            mid = len(self.list)//2
            return (self.list[mid] + self.list[mid - 1]) / 2
        else:
            return self.list[len(self.list)//2]
        
        
        