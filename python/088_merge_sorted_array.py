# https://leetcode.com/problems/merge-sorted-array/

# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# Note:
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if n != 0:
            ind = m + n - 1
            ind1 = m - 1
            ind2 = n - 1
            while (ind1 >= 0 and ind2 >= 0):
                if nums1[ind1] >= nums2[ind2]:
                    nums1[ind] = nums1[ind1]
                    ind = ind - 1
                    ind1 = ind1 - 1
                else:
                    nums1[ind] = nums2[ind2]
                    ind = ind - 1
                    ind2 = ind2 - 1
            if ind1 != 0:
                while ind2 >= 0:
                    nums1[ind] = nums2[ind2]
                    ind = ind - 1
                    ind2 = ind2 - 1