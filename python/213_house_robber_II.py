# https://leetcode.com/problems/house-robber-ii/

# Note: This is an extension of House Robber.
# After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        else:
            return max(self.rob1(nums[1:]), self.rob1(nums[:-1]))
        
    def rob1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        sum = [0]*n
        sum[0] = nums[0]
        sum[1] = max(nums[0], nums[1])
        for i in range(2, n):
            sum[i] = max(sum[i-2]+nums[i], sum[i-1])
        return sum[n-1]
        