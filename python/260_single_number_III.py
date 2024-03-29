# https://leetcode.com/problems/single-number-iii/

# Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
# For example:
# Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].
# Note:
# The order of the result is not important. So in the above example, [5, 3] is also correct.
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def singleNumber(self, nums):
        dic = {}
        for n in nums:
            if dic.has_key(n) == False:
                dic[n] = 1
            else:
                dic.pop(n)
        return dic.keys()