'''
Backspace String Compare

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
'''
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        #this function generates a new string with the backspace
        def getNew(str): 
            i = 0 
            while(i < len(str)): #iterate through the string 
                if str[i] == "#": #if you encounter a '#'
                    if i > 0: #if the character is not the first character
                        str = str[:i-1] + str[i+1:] #delete whatever character was before # 
                        i = 0 #start over from the beginning of string 
                        continue
                    if i == 0: #if first character
                        str = str[i+1:]   #just delete the # because it doesn't matter
                        i = 0 #start over from the beginning of string
                        continue
                i += 1 #if not a #, go on to the next character
            return str 

        return getNew(S) == getNew(T)

        
