# https://leetcode.com/problems/kth-largest-element-in-an-array/

# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.

class Solution(object):
    # An easy AC way. O(n log n).
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        nums.sort()
        n = len(nums)
        return nums[n-k]

    # O(n) solution. 
    # Ref: http://www.cs.yale.edu/homes/aspnes/pinewiki/QuickSelect.html
    def findKthLargest_1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import random
        pivot = random.choice(nums)
        nums1, nums2 = [], []
        for num in nums:
            if num > pivot:
                nums1.append(num)
            elif num < pivot:
                nums2.append(num)
        if k <= len(nums1):
            return self.findKthLargest(nums1, k)
        if k > len(nums) - len(nums2):
            return self.findKthLargest(nums2, k - (len(nums) - len(nums2)))
        return pivot
        