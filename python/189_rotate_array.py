class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        idx = 0
        distance = 0
        cur = nums[0]
        for x in range(n):
            next = (idx + k) % n
            temp = nums[next]
            nums[next] = cur
            idx = next
            cur = temp
            
            distance = (distance + k) % n
            if distance == 0:
                idx = (idx + 1) % n
                cur = nums[idx]