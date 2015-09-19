# https://leetcode.com/problems/h-index-ii/

# Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?
# Hint:
# Expected runtime complexity is in O(log n) and the input is sorted.

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) / 2
            if citations[mid] >= n - mid:
                right = mid - 1
            else:
                left = mid + 1
        return n - left
