# https://leetcode.com/problems/two-sum/

# Given an array of integers, find two numbers such that they add up to a specific target number.
# The function twoSum should return indices of the two numbers such that they add up to the target,
# where index1 must be less than index2. 
# Please note that your returned answers (both index1 and index2) are not zero-based.

# You may assume that each input would have exactly one solution.
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictN = {}
        for i in range(0, len(nums)):
            if dictN.has_key(target-nums[i]):
                key = target-nums[i]
                return (dictN[key], i+1)
            else:
                dictN[nums[i]] = i+1
                