class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # We use "last" to keep track of the maximum distance that has been reached
        # by using the minimum steps "ret", whereas "curr" is the maximum distance
        # that can be reached by using "ret+1" steps. Thus,curr = max(i+A[i]) where 0 <= i <= last.

        ret = 0
        last = 0
        curr = 0
        for i in range(len(nums)):
            if i > last:
                last = curr
                ret += 1
            curr = max(curr, i+nums[i])
        return ret
# Greedy! Not Dynamic Programming!