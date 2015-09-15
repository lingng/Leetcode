# https://leetcode.com/problems/permutations-ii/

# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
# For example,
# [1,1,2] have the following unique permutations:
# [1,1,2], [1,2,1], and [2,1,1].

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
            
        # contains duplicate. but the order of the original list does not matter.
        nums.sort()
        result = []
        previousNum = None
        for i in range(len(nums)):
            if nums[i] == previousNum: 
                continue
            previousNum = nums[i]
            for j in self.permuteUnique(nums[:i] + nums[i+1:]):
                result.append([nums[i]] + j)
        return result