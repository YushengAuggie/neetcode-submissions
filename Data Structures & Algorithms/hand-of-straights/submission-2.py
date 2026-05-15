from collections import Counter
import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        counter = Counter(hand)
        heapq.heapify(hand)
        cur_group = []

        while hand:
            next_round = []
            cur_group = groupSize
            prev_val = None
            # pop out the smallest value
            cur = heapq.heappop(hand)
            if counter[cur] == 0:
                continue
            counter[cur] -= 1
            for nxt in range(cur + 1, cur + groupSize):
                if nxt in counter and counter[nxt] > 0:
                    counter[nxt] -= 1
                else:
                    return False
        return True