'''
Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        '''
        IDEA: 
        
        We know that to create a valid string, we must know the remaining counts of opening and closing. 
        
        
        Always think of the base case first: when opens and close both equal 0, add the string to result array.
        
        If the above condition isn't met: 
        
        if opens is greater than 0, add "(" to the existing string and decrement opens, passing this to helper 
        if opens is less than closing, add ")" to the existing string and decrement close, passing this to helper 
        
        idea is that we want to create string and decrement opens/close counts in each recursive call.
        '''
        res = []
        
        def helper(s, opens, close): 
            if opens == 0 and close == 0: 
                res.append(s)
                return
            if opens>0: 
                helper(s +"(", opens-1, close)
            if opens<end: 
                helper(s+ ")", opens, close-1)
                
        helper("", n, n)
        return res
