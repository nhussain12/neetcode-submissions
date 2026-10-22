# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length, tmp = 0, head

        while tmp:
            length += 1 
            tmp = tmp.next

        target_index = length - n 

        dummy = ListNode(0, head)
        counter, curr, prev = 0, head, dummy
        while counter != target_index:
            counter += 1
            prev = curr
            curr = curr.next

        prev.next = curr.next

        return dummy.next
        