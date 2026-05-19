# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        print(id(head))
        id_set = {id(head)}

        while head:
            if id(head.next) in id_set:
                return True
            id_set.add(id(head.next))
            head = head.next
        
        return False