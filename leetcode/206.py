# 206 Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/ - Easy

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        rest = None
        while head is not None:
            rest = new_head
            new_head = ListNode(val=head.val)
            new_head.next = rest
            head = head.next

        return new_head
