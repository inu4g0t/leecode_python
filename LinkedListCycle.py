# https://oj.leetcode.com/problems/linked-list-cycle/

# Given a linked list, determine if it has a cycle in it.

# Follow up:
# Can you solve it without using extra space?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if not head:
            return False
        n1=head
        n2=head
        while not not n2:
            n2 = n2.next
            if not n2:
                return False
            n2 = n2.next
            n1 = n1.next
            if n1 is n2:
                return True
        return False
