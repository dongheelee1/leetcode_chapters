'''
Plus One

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''
class Solution:
    
    def plusOne(self, digits: List[int]) -> List[int]:
        '''
        IDEA: 
        
        1. add 1 to the last digit. Is this greater than 9? 
            -a. If so, make the current digit 0 and record carry = 1
            -b. If not, add 1 to the last digit and return the modified digits array 
        
        2. If a. holds from 1., this means we have to carry over 1 to the next digit in question. 
           So start from the second to last digit.
           Similarly, add carry to the current digit. Is this greater than 9? 
            -c. If so, carry stays 1 and make the current digit 0
            -d. If not, just add carry to the current digit 
            
        3. If there is still something in carry, return new digits which is [1] + digits
        '''
        #1
        if digits[-1] + 1 > 9: 
            digits[-1] = 0 
            carry = 1
        else: 
            digits[-1] += 1
            return digits 
        
        #2. 
        for i in range(len(digits)-2, -1, -1): 
            #logic
            if digits[i] + carry > 9: 
                digits[i] = 0
                #carry keeps being 1 
            else:
                digits[i] += carry #for test case [8, 9, 9] => [9, 9, 9]
                carry = 0 
                break
            
        if carry: 
            digits = [1] + digits #for test case [9, 9, 9] which becomes [1, 0, 0, 0]
            
        return(digits)
