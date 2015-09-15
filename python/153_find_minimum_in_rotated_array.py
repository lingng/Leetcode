# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# Find the minimum element.
# You may assume no duplicate exists in the array.

class Solution(object):
    def findMin_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            # Might include the situation that the array does not rotate.
            if nums[start] > nums[mid] and nums[mid] < nums[end]:
                end = mid
            elif nums[start] < nums[mid] and nums[mid] > nums[end]:
                start = mid
            else:
                break
        return min(nums[start], nums[end])

    # Faster solution.
    def findMin_2(self, num):
        rst = num[0]
        start, end = 0, len(num) - 1
        while start <= end:
            mid = (start + end)/2
            if num[mid] >= rst:
                start = mid + 1
            else:
                rst = num[mid]
                end = mid
        return rst