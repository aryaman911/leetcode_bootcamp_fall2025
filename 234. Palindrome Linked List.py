# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Step 1: Copy all values from the linked list into a Python list
        values = []
        current = head
        while current is not None:
            values.append(current.val)
            current = current.next

        # Step 2: Check if list is a palindrome
        left = 0
        right = len(values) - 1

        while left < right:
            if values[left] != values[right]:
                return False
            left += 1
            right -= 1

        return True
