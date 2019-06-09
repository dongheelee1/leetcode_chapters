'''
5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''
class Solution(object):
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''
        IDEA: 
        
        go through each char in s 
        
        the idea is that the current char we are on is the center of the possible palindrome and we want to expand outwards opposite this center 
        
        this possible palindrome can be either even or odd in length
        
        consider both cases 
        for even: pass in left: i and right: i+1
        for odd: pass in left: i and right: i 
        
        getPalindrome takes this parameters and expands left and right while chars at these pointers are equal, the final result is the palindromic substring 
        
        return curr_max string
        
        '''
        #check palindrome going from inner to outer 
        def getPalindrome(left, right): 
            
            while left >= 0 and right < len(s) and s[left] == s[right]: 
                left -= 1
                right += 1

            return s[left+1:right]
        
        curr_max = ""
        
        for i in range(len(s)): 
            even = getPalindrome(i, i+1)
            odd = getPalindrome(i, i)
            curr_max = max(curr_max, odd, even, key=len)

        return curr_max
