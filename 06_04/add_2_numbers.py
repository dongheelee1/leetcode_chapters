'''
Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def helper(l1, l2, carry): 
            if l1 is None and l2 is None: 
                if carry: 
                    return ListNode(carry)
                return None 

            if l1 is None and l2: 
                if not carry: 
                    return l2 
                else: 
                    s = l2.val + carry
                    if s > 9:
                        s = (s) % 10
                        carry = 1
                    else: 
                        carry = 0 
                    newl2 = ListNode(s)
                    newl2.next = helper(None, l2.next, carry)
                    return newl2 


            if l2 is None and l1: 
                if not carry: 
                    return l1 
                else: 
                    s = l1.val + carry
                    if s > 9:
                        s = (s) % 10
                        carry = 1
                    else: 
                        carry = 0 
                    newl1 = ListNode(s)
                    newl1.next = helper(l1.next, None, carry)
                    return newl1

            s = l1.val + l2.val + carry
            if s > 9: 
                s = (s) % 10 
                carry = 1
            else: 
                carry = 0 
            l1.val = s
            l1.next = helper(l1.next, l2.next, carry) 
            return l1 

        return helper(l1, l2, 0)
