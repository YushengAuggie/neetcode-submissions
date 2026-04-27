# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def _merge_lists(self, h1: ListNode, h2: ListNode) -> ListNode:
        """Merging two lists, in ascending order, returns new head."""
        dummy = head = ListNode(float("-inf"))
        while h1 and h2:
            if h1.val < h2.val:
                dummy.next = h1
                h1 = h1.next
            else:
                dummy.next = h2
                h2 = h2.next
            dummy = dummy.next
        dummy.next = h1 or h2
        return head.next

        
        


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        The easiest way is to put all the elements from all the lists and then sort them together.
        It would take
        O(nlogn) time, n is the total length of the elements
        space is O(n), which is the return list size

        optimized:
        we can have a pointer, loop through all the head, and then find the min, and add it to the 
        return list. which will take
        say we have m sub-lists, we will need to compare a number with all other nodes
        n^2 time, n space

        optimized way 2, we can have a heapq, and puting things to there, and always pop out the min valud and
        add it to the return list, which is also nlogn time, and n space.

        so, according to the hint, we want to merge lists, like l1 and l2 -> l1, and then l1 and l3 ... till l1 and lk.
        so it is like, we n * k, n is the length of the element and k is the number of lists
        """
        if not lists:
            return None
        
        l1 = lists.pop()
        while lists:
            l2 = lists.pop()
            l1 = self._merge_lists(l1, l2)
        return l1


