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
        result = []
        for i in range(0, len(nums)):
            for j in self.permuteUnique(nums[:i]+nums[i+1:]):
                # print [nums[i]]+j
                result.append([nums[i]]+j)
        return result

# Cannot AC in Online Judge.
x = Solution()
print x.permuteUnique([0,3,2,1,1,1])