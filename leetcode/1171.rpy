# 1171 Remove Zero Sum Consecutive Nodes from Linked List

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []

        trav = head

        while trav is not None:
            lst.append(trav.val)
            trav = trav.next

        print("lst-pre", lst)
        lst = self.removeZeroSumList(lst)
        print("lst-post", lst)

        new_head = None
        if len(lst) <= 0:
            return new_head

        new_head = ListNode(lst[0])
        prev = new_head

        for val in lst[1:]:
            prev.next = ListNode(val)
            prev = prev.next

        return new_head

    def removeZeroSumList(self, lst: List[int]) -> List[int]:
        if len(lst) <= 0:
            return []

        slow = len(lst) - 1
        while slow >= 0:
            fast = slow
            while fast >= 0:
                intermed_sum = sum(lst[fast:slow])
                if intermed_sum == 0:
                    spliced = lst[0:fast] + lst[slow + 1 : -1]
                    print(spliced)
                    return self.removeZeroSumList(spliced)
                fast -= 1
            slow -= 1

        return lst
