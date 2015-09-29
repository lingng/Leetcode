# https://leetcode.com/problems/find-the-duplicate-number/

# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
# Note:
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated more than once.

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Idea similar to bucket sort:
        # Sort the array to fix the nums[i] = i+1 format.
        # If the destination position already has the fixed number, then return the number. 
        # This should be the duplicate number.
        for i in range(0, len(nums)):
            if nums[i] == i+1:
                continue
            else:
                while nums[i] != i+1:
                    if nums[nums[i]-1] != nums[i]:
                        print i, nums[i]
                        tmp = nums[nums[i]-1]
                        nums[nums[i]-1] = nums[i]
                        nums[i] = tmp
                        print nums
                    else:
                        return nums[i]
        print nums

x = Solution()
print x.findDuplicate([8,7,1,10,17,15,18,11,16,9,19,12,5,14,3,4,2,13,18,18])