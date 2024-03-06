class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        c = ListNode(0)
        x = c

        while list1 is not None and list2 is not None: 
            if list1.val < list2.val:
                x.next = list1
                list1 = list1.next
            else:
                x.next = list2
                list2 = list2.next

            x = x.next

        if list1 is not None:
            x.next = list1
        else:
            x.next = list2

        return c.next