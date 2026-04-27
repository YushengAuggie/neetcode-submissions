# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class NodeWrapper:
    def __init__(self, node):
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # heapq solution
        # nlogn time
        # O(k) space
        cur = dummy = ListNode(float("-inf"))
        priority_queue = []

        for i in range(len(lists)):
            if lists[i] is not None:
                heapq.heappush(priority_queue, NodeWrapper(lists[i]))

        while priority_queue:
            new_min = heapq.heappop(priority_queue).node
            cur.next = new_min
            cur = new_min
            if new_min.next:
                heapq.heappush(priority_queue, NodeWrapper(new_min.next))
        return dummy.next