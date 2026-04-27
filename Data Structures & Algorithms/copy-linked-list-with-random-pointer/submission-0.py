"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Easiest way:
        we build the new list first, and at the same time we build a map
        that maps old node -> corresponding new node
        And then we go over the list again and assign the random 
        time: O(n)
        space: O(n)
        """ 
        dummy = Node(-1)
        cur = head
        prev = dummy
        old_new_node_map = {}
        while cur:
            new_node = Node(cur.val)
            old_new_node_map[cur] = new_node
            prev.next = new_node
            prev = new_node
            cur = cur.next
        
        cur = head
        cur_new = dummy.next
        while cur:
            old_random = cur.random
            if old_random:
                new_random = old_new_node_map[old_random]
                cur_new.random = new_random
            cur = cur.next
            cur_new = cur_new.next
        return dummy.next


         