# https://leetcode.com/problems/combinations/

# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
# For example,
# If n = 4 and k = 2, a solution is:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

class Solution(object):
    def helper(self, nums, k, start, stack, result):
        if len(stack) == k:
            result.append(stack)
        else:
            for i in range(start, len(nums)):
                self.helper(nums, k, i+1, stack+[nums[i]], result)
                
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        rst = []
        nums = []
        for i in range(1, n+1):
            nums.append(i)
        self.helper(nums, k, 0, [], rst)
        return rst