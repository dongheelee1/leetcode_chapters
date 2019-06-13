'''
Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #we could traverse nums arr in one pass 
        '''
        in the for 
        '''
        curr_max_product = nums[0]
        curr_min_product = nums[0]
        prev_max_product = nums[0]
        prev_min_product = nums[0]
        curr = nums[0] #we need this for the case that nums contains only one element 
        
        for i in range(1, len(nums)): 
            #-1, 6, 2, -2 --> max is 24 (-1, 6, 2, -2) this means that 
            #when i=3, the curr_max_product = 12, curr_min_product = -12, curr = -2
            #curr_max_product = max(12*-2, -12*-2, -2) 
            #curr = max(12, 24) = 24 
            curr_max_product = max(prev_max_product*nums[i], prev_min_product*nums[i], nums[i])
            curr_min_product = min(prev_max_product*nums[i], prev_min_product*nums[i], nums[i])
            curr = max(curr, curr_max_product)
            prev_max_product = curr_max_product #update prev_max_product 
            prev_min_product = curr_min_product #update prev_min_product
        return curr
