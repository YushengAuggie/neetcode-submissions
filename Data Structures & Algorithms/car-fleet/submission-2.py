class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        time: O(nlogn)
        space: O(n)
        """
        pos_speed = []
        for pos, s in zip(position, speed):
            pos_speed.append((pos, s))
        
        pos_speed.sort(reverse=True)
        fleet = 0
        prev_slowest_time = 0
        for pos, s in pos_speed:
            arrival_time = (target - pos) / s
            if arrival_time > prev_slowest_time:
                prev_slowest_time = arrival_time
                fleet += 1
        return fleet

