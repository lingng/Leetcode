# https://leetcode.com/problems/majority-element-ii/
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.

import math

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        limit = math.floor(length/3)
        dic = {}
        result = []
        for i in range(0, length):
            if dic.has_key(nums[i]):
                dic[nums[i]] = dic[nums[i]] + 1
            else:
                dic[nums[i]] = 1
        for key in dic:
            if dic[key] > limit:
                result.append(key)
        return result

x = Solution()
nums = [1]
print x.majorityElement(nums)
