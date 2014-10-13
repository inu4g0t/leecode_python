# https://oj.leetcode.com/problems/merge-two-sorted-lists/

# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if not l2:
            return l1
        if not l1:
            return l2
        if l1.val < l2.val:
            tmp=l1
            l1 = l1.next
            tmp.next = None
            head = tmp
        else:
            tmp=l2
            l2 = l2.next
            tmp.next = None
            head = tmp
        cur = head
        while True:
            if not l1:
                cur.next = l2
                return head
            if not l2:
                cur.next = l1
                return head
            if l1.val < l2.val:
                tmp = l1
                l1 = l1.next
                tmp.next = None
                cur.next = tmp
                cur = cur.next
            else:
                tmp = l2
                l2 = l2.next
                tmp.next = None
                cur.next = tmp
                cur = cur.next
