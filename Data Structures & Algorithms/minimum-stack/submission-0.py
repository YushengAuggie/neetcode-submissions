import bisect
class MinStack:

    def __init__(self):
        self.values = []
        self.min_vals = []
        

    def push(self, val: int) -> None:
        self.values.append(val)
        if self.min_vals:
            self.min_vals.append(min(self.min_vals[-1], val))
        else:
            self.min_vals.append(val)

    def pop(self) -> None:
        self.values.pop()
        self.min_vals.pop()
        

    def top(self) -> int:
        return self.values[-1]
        

    def getMin(self) -> int:
        return self.min_vals[-1]
        
