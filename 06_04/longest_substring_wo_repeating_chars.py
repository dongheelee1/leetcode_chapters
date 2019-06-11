'''
Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
class Solution(object):
    
    '''
    IDEA: 
    
    keep "used" dictionary where key is the character and the value is the current character's index 
    set max length, start to 0 
    
    iterate through each index, character tuple 
    
    if current character is already used and if the current start of the max length substring is less than/equal to the index of the character already in used, then we want to reset start of the max length substring (since we've run into a repeat character)
    
    otherwise if character has not been used, we want to continuously update the max length of the substring substracting the start from current index i adding 1 
    
    in each iteration, update the index of current character
    '''
    #"abcabcbb"
    #"tmmzuxt"

    def lengthOfLongestSubstring(self, s):
        used = {} 
        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]: #for the second condition, consider test "tmmzuxt", we only want to reset start when it's start index <= used[c] --> 0 but obv start idx is 2 and used[c] is 0
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)

            used[c] = i



        return max_length
    
