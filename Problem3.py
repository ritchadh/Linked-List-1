# 142. Linked List Cycle II

# Time Complexity: O(N)
# Space Complexity: O(N)
# Did this code successfully run on Leetcode: all test cases passed
# Any problem you faced while coding this: No

# Approach: using a set and checking if the node is already present in the hash set

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        myset = set()
        curr = head
        
        while(curr!=None):
            
            if curr in myset:
                return curr
            
            myset.add(curr)
            curr = curr.next
            