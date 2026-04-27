import heapq

class MedianFinder:

    def __init__(self):
        # two heaps
        self.small = [] # we use the negated value 
        self.large = [] 

    def addNum(self, num: int) -> None:
        if self.large and self.large[0] < num:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)

        if len(self.small) > len(self.large) + 1:
            largest_in_small = heapq.heappop(self.small)
            heapq.heappush(self.large, -largest_in_small)
        elif len(self.large) > len(self.small):
            smallest_in_large = heapq.heappop(self.large)
            heapq.heappush(self.small, -smallest_in_large)

    def findMedian(self) -> float:
        if (len(self.small) + len(self.large)) % 2 == 0:
            return (-self.small[0] + self.large[0]) / 2
        else:
            return -self.small[0]
        
    # def findMedian(self) -> float:
    #     if len(self.small) > len(self.large):
    #         return -1 * self.small[0]
    #     elif len(self.large) > len(self.small):
    #         return self.large[0]
    #     return (-1 * self.small[0] + self.large[0]) / 2.0