from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        self.values = defaultdict(list) # key, (timestamp, value)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.values[key]
        if not values:
            return ""
        start = 0
        end = len(values) - 1
        valid_timestamp = 0
        valid_value = ""
        while start <= end:
            mid = (start + end) // 2
            mid_timestamp, mid_value = values[mid] 
            if mid_timestamp == timestamp:
                return mid_value
            elif mid_timestamp < timestamp:
                # valid
                # we want the lagest valid timestamp
                if mid_timestamp > valid_timestamp:
                    valid_timestamp = mid_timestamp
                    valid_value = mid_value
                start = mid + 1
            else:
                end = mid - 1
        return valid_value

        #idx = bisect.bisect_left(values, (timestamp, ""))
        #if idx == len(values):
        #    idx = idx - 1
#
        #prev_timestamp, prev_value = values[idx]
        # return prev_value


        
