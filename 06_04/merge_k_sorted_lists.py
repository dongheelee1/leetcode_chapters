'''
23. Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    '''
    IDEA: 
    
    - initialize a priority queue (binary tree with each root being smaller than both of its children)
    
    - go through each list in the list of lists, adding node to the min heap 
    
    - set up a linked list first set to to dummy node 
    
    - go through each node in the min heap and pop each root off to the linked list 
    
    - return the head of the new list 
    '''
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        import queue
        q = queue.PriorityQueue()
        
        for l in lists: 
            head = l 
            while head is not None: 
                q.put(head.val)
                head = head.next 
        
        new = ListNode(-1)
        current = new

        while not q.empty():
            current.next = ListNode(q.get())
            current = current.next
        return new.next
    
