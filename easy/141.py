# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: # if there is no head or there is no next for head, return false
            return False

        slow = head # set slow pointer to the head
        fast = head.next # set fast pointer to the next node

        while slow != fast: # while slow is not equal to fast pointer
            if not fast or not fast.next: # if fast or fast.next is not a node, the there is no loop
                return False
            
            slow = slow.next # set to the next node 1 step
            fast = fast.next.next # set to the next next node 2 step

        return True
