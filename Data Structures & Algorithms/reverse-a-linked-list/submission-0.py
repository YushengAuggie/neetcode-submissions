# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        iterate the whole linked list
        and record the prev node. 
        and then 
        a ->    b ->    c
        ^.      ^.      ^
        prev.   cur.    next
        
        cur -> prev 
        prev = cur
        cur = cur.next
        """
        
        if not head:
            return head
        
        prev = None
        cur = head # 0
        while cur:
            next_node = cur.next # 1 2 3
            cur.next = prev # 0->None 1->0 2->1
            prev = cur # prev = 0 1 
            cur = next_node # cur = 1 2
        return prev