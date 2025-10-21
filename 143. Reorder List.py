# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Step 1: collect nodes into an array
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        # Step 2: relink from both ends toward the middle
        i, j = 0, len(nodes) - 1
        while i < j:
            # link i -> j
            nodes[i].next = nodes[j]
            i += 1
            if i == j:
                break
            # link j -> i
            nodes[j].next = nodes[i]
            j -= 1

        # Step 3: terminate the list
        nodes[i].next = None
