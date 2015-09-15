# https://leetcode.com/problems/house-robber/

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Dynamic Programming.
        # For each house, has two choices: take the money, do not take the money. 
        # SUM[i] = MAX(SUM[i-2]+NUM[i], SUM[i-1])
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