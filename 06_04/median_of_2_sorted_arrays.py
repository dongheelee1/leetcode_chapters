class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        Median of Two Sorted Arrays

        There are two sorted arrays nums1 and nums2 of size m and n respectively.

        Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

        You may assume nums1 and nums2 cannot be both empty.

        Example 1:

        nums1 = [1, 3]
        nums2 = [2]

        The median is 2.0
        Example 2:

        nums1 = [1, 2]
        nums2 = [3, 4]

        The median is (2 + 3)/2 = 2.5
        
        1. merge nums1 and nums2 into a sorted array using the merge algorithm 
        2. if merged is even (divisible by 2), then return the sum(middle element and the element before middle)/2
        3. if merged is uneven, return the middle element 
        '''
        
        i = 0 
        j = 0 
        merged = []
        while i < len(nums1) and j < len(nums2): 
            
            if nums1[i] <= nums2[j]: 
                merged.append(nums1[i])
                i += 1
            else: 
                merged.append(nums2[j])
                j += 1

        
        if i < len(nums1): 
            merged += nums1[i:]
        if j < len(nums2): 
            merged += nums2[j:]

        if len(merged) % 2 == 0: 
            num = (merged[len(merged)//2] + merged[len(merged)//2-1])/2
            return num
        else: 
            return merged[len(merged)//2]
