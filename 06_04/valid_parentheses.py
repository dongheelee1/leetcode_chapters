'''
Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''
class Solution:
    def isValid(self, s: str) -> bool:
        '''
        if length of s is odd, then return False 
        initialize a stack of opening parantheses 
        
        go through the given string s character by character
            a. if the character is an open character, push to the top of stack
            b. if the char is a closing character, check to see if 
                1. the stack is not empty 
                2. the top of the stack is the corresponding open character
                
                if all of the above are satisfied, pop off the last character in the stack 
            c. if a. and b. are not met, return False
            
        if there are still contents in stack, return False
        return True 
        '''
        if len(s) % 2 != 0: 
            return False
        
        st = []
        
        for i in s: 
            if i == "(" or i == "{" or i == "[": 
                st.append(i)
            elif i == ")" and len(st) != 0: 
                if st[-1] == "(": 
                    st.pop()
                else: 
                    return False
            elif i == "]" and len(st) != 0: 
                if st[-1] == "[": 
                    st.pop()
                else: 
                    return False
            elif i == "}" and len(st) != 0: 
                if st[-1] == "{": 
                    st.pop()
                else: 
                    return False 
            else: 
                return False
        
        if len(st) != 0: 
            return False
        
        return True 
        
