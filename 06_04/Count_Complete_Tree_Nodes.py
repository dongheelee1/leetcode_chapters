# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Count Complete Tree Nodes

Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6




IDEA: 
At each node encounter, increment self count 
If you reach end of the tree (aka current node is None, backtrack / return)
Search the tree using a DFS strategy 
    - helper(r.left)
    - helper(r.right)
    
'''
class Solution:
    def countNodes(self, root: TreeNode) -> int:

        self.count = 0 
        
        def helper(r): 
            
            if r is None: 
                return #backtrack 
            
            self.count += 1
            
            helper(r.left)
            helper(r.right)
            
        helper(root)
        
        return self.count
            
