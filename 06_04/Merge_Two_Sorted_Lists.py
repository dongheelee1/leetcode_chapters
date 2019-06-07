'''
Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None 
        if l1 is None and l2: 
            return l2 
        if l1 and l2 is None: 
            return l1 
        
        if l1.val < l2.val: 
            new = l1
            new.next = self.mergeTwoLists(l1.next, l2)
        else: 
            new = l2
            new.next = self.mergeTwoLists(l1, l2.next)
        return new 
