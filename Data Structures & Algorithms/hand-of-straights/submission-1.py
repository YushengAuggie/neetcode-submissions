class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        The easiest way is to simulate that by sorting them first and then putting those elements into groups. To do that, every time we just pick one value and then the next value. We know how many values will be in each group, so we just construct it. Then we use another number from the key (like the list that is available), and if it is not available, you should remove it.opy
        len(hand)/groupSize = group number n
        m = len(hand)
        time O(m^2 / groupSize)
        space O(hand)
        """
        
        cur_group = []
        hand.sort(reverse=True)
        while hand:
            next_round = []
            start_hand = len(hand)
            while hand:
                cur = hand.pop()
                if not cur_group or cur_group[-1] + 1 == cur:
                    cur_group.append(cur)
                else:
                    next_round.append(cur)
                if len(cur_group) == groupSize:
                    cur_group = []
                    break
            if len(next_round) == start_hand:
                return False
            while next_round:
                hand.append(next_round.pop())
        return len(cur_group) == 0
            


            

            
       