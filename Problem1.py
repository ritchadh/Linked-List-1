# 206. Reverse Linked List

# Time Complexity: O(n)
# Space Complexity: O(1)
# Did this code successfully run on Leetcode: all test cases passed
# Any problem you faced while coding this: No

# Approach: use 2 pointers prev and curr to navigate the list and reverse it

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        curr = head
        
        while(curr!=None):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        head = prev
        return head
