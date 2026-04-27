# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # step 1 find the split
        # step 2 reverse the second half
        # step 3 merge the two half
        # time: O(n) space: O(1)
        # if not head or not head.next:
        #     return 

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None

        # slow start of the second half
        prev = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node

        # prev is the largest one now
        first_half_p = head
        second_half_p = prev
        while first_half_p and second_half_p:
            next_first = first_half_p.next
            next_second = second_half_p.next
            
            first_half_p.next = second_half_p
            second_half_p.next = next_first

            first_half_p = next_first
            second_half_p = next_second



