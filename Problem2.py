# 19. Remove Nth Node From End of List

# Time Complexity: O(N); worst case complexity
# Space Complexity: O(1); 
# Did this code successfully run on Leetcode: all test cases passed
# Any problem you faced while coding this: No

# Approach: Using 2-pointer approach; move second pointer n steps ahead and keep moving the pointer 1 (from head) and pointer
# 2 until the 2nd pointer reaches 'None'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        ptr1 = head
        ptr2 = head
        
        for i in range(0,n):
            ptr2 = ptr2.next
        
        if ptr2 == None:
            head = ptr1.next
            return head
        
        while(ptr2.next!=None):
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        ptr1.next = ptr1.next.next
        return head