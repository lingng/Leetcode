# https://leetcode.com/problems/majority-element/

# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        dictA = {}
        length = len(num)
        for element in num:
            if element in dictA:
                dictA[element] = dictA[element]+1
            else:
                dictA[element] = 1
        for element in dictA:
            if dictA[element] > length / 2:
                return element