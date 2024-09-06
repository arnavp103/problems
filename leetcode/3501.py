# 3501 Delete Nodes From Linked List Present in Array
# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/ - Medium

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(
        self, nums: list[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        blocked = set(nums)
        new_head = head
        while new_head and new_head.val in blocked:
            new_head = new_head.next
        if new_head is None:
            return None

        prev = new_head
        end = new_head.next

        while end:
            if end.val in blocked:
                end = end.next
                continue
            # if not blocked add the value to the list
            prev.next = end
            prev = end
            end = end.next

        # since the end should have become None
        prev.next = None

        return new_head
