# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        first = head
        second = prev
        maximum = 0
        while second:
            maximum = max(maximum,first.val + second.val)
            first = first.next
            second = second.next
        return maximum


        