# https://leetcode.com/problems/product-of-array-except-self/
# Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
# Solve it without division and in O(n).
# For example, given [1,2,3,4], return [24,12,8,6].

class Solution(object):
    # This function does not use division.
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        output = [1]*length
        
        left = 1
        right = 1
        # Left -> right. Calculate the product of the first element to the current element
        # Assign it to the next output array
        for i in range(0, length - 1):
            left = left * nums[i]
            output[i+1] = output[i+1]*left
        # Right -> left. Calculate the product of the last element to the current element
        # Multiply it with the previous result.
        for i in range(length - 1, 0, -1):
            right = right * nums[i]
            output[i-1] = output[i-1]*right
        return output

    # This function uses division. 
    def productExceptSelf_1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numForZero = 0
        product = 1
        for i in range(0, len(nums)):
            if nums[i] == 0:
                numForZero = numForZero + 1
            else:
                product = product * nums[i]
        if numForZero == 0:
            for i in range(0, len(nums)):
                nums[i] = product / nums[i]
        elif numForZero == 1:
            for i in range(0, len(nums)):
                if nums[i] == 0:
                    nums[i] = product
                else:
                    nums[i] = 0
        else:
            for i in range(0, len(nums)):
                nums[i] = 0
        return nums