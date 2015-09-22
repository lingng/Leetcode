# https://leetcode.com/problems/kth-largest-element-in-an-array/

# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.

class Solution(object):
    # An easy AC way. But not a good solution.
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        nums.sort()
        n = len(nums)
        return nums[n-k]
        