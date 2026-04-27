# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:    
    def _merge_lists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            return l1 or l2

        cur = dummy = ListNode(float("-inf"))
        while l1 and l2:
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
                
            
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # devide and conquer
        # merge sub-lists, till lists only has one sublist and return it
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            merged_list = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                new_head = self._merge_lists(l1, l2)
                merged_list.append(new_head)
            lists = merged_list
        return lists[0]