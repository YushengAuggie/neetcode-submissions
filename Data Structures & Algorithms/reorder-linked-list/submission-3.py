# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # step 1 find the split
        # step 2 reverse the second half
        # step 3 merge the two half
        # time: O(n) space: O(1)
        if not head or not head.next:
            return 
            
        slow = fast = head
        prev_slow = None
        while fast and fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next
        if prev_slow:
            prev_slow.next = None

        # slow start of the second half
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        # prev is the largest one now
        first_half_p = head.next
        second_half_p = prev
        use_first_half = False
        cur = head
        while cur and first_half_p and second_half_p:
            if use_first_half:
                cur.next = first_half_p
                first_half_p = first_half_p.next
            else:
                cur.next = second_half_p
                second_half_p = second_half_p.next
            use_first_half = not use_first_half
            cur = cur.next

        cur.next = first_half_p or second_half_p



