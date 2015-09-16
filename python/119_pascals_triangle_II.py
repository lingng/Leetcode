# https://leetcode.com/problems/pascals-triangle-ii/

# Given an index k, return the kth row of the Pascal's triangle.
# For example, given k = 3,
# Return [1,3,3,1].
# Note:
# Could you optimize your algorithm to use only O(k) extra space?

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        rst = [1]
        lst = [1, 1]
        while len(rst) < rowIndex+1:
            rst = [1]
            for i in range(1, len(lst)):
                rst.append(lst[i] + lst[i-1])
            rst.append(1)
            lst = rst
        return rst