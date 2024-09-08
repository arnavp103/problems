# 725 Split Linked List in Parts
# https://leetcode.com/problems/split-linked-list-in-parts/ - Medium

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> list[Optional[ListNode]]:
        # Calculate the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        # Calculate the size of each part
        part_size = length // k
        extra = length % k

        parts = []

        def get_part(head, size):
            if not head:
                return None
            current = head
            for _ in range(size - 1):
                if current.next:
                    current = current.next

            next_node = current.next
            current.next = None
            return next_node

        current = head
        for _ in range(k):
            parts.append(current)
            current = get_part(current, part_size + (1 if extra > 0 else 0))
            extra -= 1

        return parts
