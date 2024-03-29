'''
15. 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [] 
        nums.sort() 
        
        for i in xrange(0, len(nums)-2): 
            
            if i > 0 and nums[i] == nums[i-1]: #this is to avoid duplicate
                continue
            left = i+1 
            right = len(nums)-1
            
            while left < right: 
                total = nums[i] + nums[left] + nums[right]
                if total < 0: 
                    left += 1 
                elif total > 0: 
                    right -= 1
                elif total == 0: 

                    res.append([nums[i], nums[left], nums[right]])
                    while left<right and nums[left+1] == nums[left]: 
                        #shift left pointer so that next element is new/not repeated
                        left += 1
                    while left<right and nums[right-1] == nums[right]:
                        #shift right pointer so that next element is new/not repeated
                        right -= 1
                    left += 1 
                    right -= 1


        return res
