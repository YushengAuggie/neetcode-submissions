# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        brute force way is to put the list to a list and we can get -n from the list
        it will use O(n) time and O(n) space
        ----

        we can use two pointer and let the time to stay the O(n) but save the space -> O(1)
        p1 = p2 = 0
        we move the p2 n steps first, and then move p1 and p2 keep moving to the end
        when p2 -> end, the p1 should be pointing to the previous node of nth from the end

        e.g.:
        idx  0 1 2 4.   n = 2
            [1,2,3,4]
         p1. ^
         p2.     ^

         p1.   ^
         p2.       ^

         edge case are we need to handle:
         1. len < n --> return []
         2. removed head -> need dummy
        """ 

        p2 = head
        distance = 0
        while distance < n and p2:
            p2 = p2.next
            distance += 1

        if distance < n: 
            return []
                         
        dummy = ListNode(-1)
        dummy.next = head
        p1 = dummy       
                         
        while p2:        
            p1 = p1.next 
            p2 = p2.next 
                         
        # p2 is the None 
        # p1.next is the node needs to be removed
        p1.next = p1.next.next
        return dummy.next
                         
                         
                         
                         
                         
                         