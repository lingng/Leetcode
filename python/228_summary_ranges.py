# https://leetcode.com/problems/summary-ranges/

# Given a sorted integer array without duplicates, return the summary of its ranges.
# For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        x = 0
        size = len(nums)
        ans = []
        while x < size:
            c = x
            r = str(nums[x])
            while x + 1 < size and nums[x + 1] - nums[x] == 1:
                x += 1
            if x > c:
                r += "->" + str(nums[x])
            ans.append(r)
            x += 1
        return ans

x = Solution()
tmp = x.summaryRanges([1, 3])
print tmp