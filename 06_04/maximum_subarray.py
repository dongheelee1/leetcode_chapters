'''
Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        #brute force solution: 
        
        best = nums[0]
        runningTotal = 0 
        
        for i in range(len(nums)): 
            
            runningTotal = nums[i]
            
            if runningTotal > best: 
                best = runningTotal 
                
            for j in range(i+1, len(nums)): 
                runningTotal += nums[j]
                if runningTotal > best: 
                    best = runningTotal
        return best
        '''
        '''
        best = the current best (max) sum; initially this value is the first element in the array
        keep track of the previous running total 
        
        iterate from the second element
            check if the previous running total is greater than 0, only then does this mean there is a potential for 
            a "best" sum and add the element to the previous running total 
            if the previous running total is less than 0, forget this and set the previous running total to the current element 
            
            after the above compare the best value and previous running total, whichever is greater set it as the new best 
            
        #if previous sum is less than 0, forget it, discard the previous sum and start at the current element 
        #if previous sum is greater than 0, it is helping our running sum so add current element to the previous sum
        
        '''
 
        best = nums[0]
        prevRunningTotal = nums[0] 
        for i in range(1, len(nums)): 
            if prevRunningTotal > 0: 
                prevRunningTotal += nums[i]
            else: 
                prevRunningTotal = nums[i]
            best = max(best, prevRunningTotal)
        return best 
