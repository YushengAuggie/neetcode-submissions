# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        time: O(n)
        space: O(1)
        """
        dummy = ListNode(-1)
        carry = 0
        prev = dummy
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            cur = l1_val + l2_val + carry
            carry = cur // 10
            cur = cur % 10
            cur_node = ListNode(cur)
            prev.next = cur_node
            prev = cur_node
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            prev.next = ListNode(1)
        return dummy.next
        
            


         