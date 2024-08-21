# 2 Add Two Numbers

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        result = ListNode(val=0, next=None)
        head = result

        carry = 0

        while True:
            if l1 is not None:
                result.val += l1.val
                l1 = l1.next

            if l2 is not None:
                result.val += l2.val
                l2 = l2.next

            result.val += carry
            carry = result.val // 10
            result.val = result.val % 10

            if l1 is None and l2 is None and carry == 0:
                return head

            new_node = ListNode(val=0, next=None)
            result.next = new_node
            result = new_node
