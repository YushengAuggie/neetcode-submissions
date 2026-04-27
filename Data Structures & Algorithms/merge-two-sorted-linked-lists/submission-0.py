# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        head = prev_node = ListNode(val=-1)
        while p1 and p2:
            if p1.val <= p2.val:
                prev_node.next = p1
                p1 = p1.next
            else:
                prev_node.next = p2
                p2 = p2.next
            prev_node = prev_node.next

        if p1:
            prev_node.next = p1
        elif p2:
            prev_node.next = p2

        return head.next