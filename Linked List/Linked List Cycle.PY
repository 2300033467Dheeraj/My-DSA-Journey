# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if not head or not head.next :
            return False

        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next 
            fast = fast.next.next

            if slow == fast :
                return True
        return False