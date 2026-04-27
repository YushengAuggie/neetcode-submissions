# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        a_list = deque()
        cur = head
        prev = None 
        while cur:
            a_list.append(cur)
            prev = cur
            cur = cur.next
            prev.next = None
        
        dummy = ListNode(-1)
        cur = dummy
        from_head = True
        while a_list:
            if from_head:
                cur.next = a_list.popleft()
                from_head = False
            else:
                cur.next = a_list.pop()
                from_head = True

            cur = cur.next
