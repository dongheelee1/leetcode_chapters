'''
Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        '''
        IDEA: 
        
        have front pointer at the (n+1)th position 
        have lag pointer at head 
        
        move above pointers in tandem until front pointer points to None 
        have lag's next point to lag's next.next 
        
        return head 
        
        '''
        #this case is hit when the length of given linked list is 1 and the node to delete is 1 from the end 
        if head.next is None and n == 1: 
            return head.next 
        
        front = head 
        lag_head = lag_runner = ListNode(-1) #lag_head.next will be the return object 
        lag_runner.next = head #connect the dummy object that lag_runner is pointing to to the first node in given list
        
        #position the front pointer to be pointing to the nth node 
        while n != 0: 
            front = front.next 
            n -= 1
        
        while front != None: 
            front = front.next 
            lag_runner = lag_runner.next 
            
        #omit the nth-to-the-end node 
        lag_runner.next = lag_runner.next.next 
        
        return lag_head.next 
