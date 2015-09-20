class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])
        if m == 0 or n == 0:
            return 0
        row = [0] * n
        matrix = [row]*m
        matrix[m-1][n-1] = max(0, -dungeon[m-1][n-1])+1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                down = None
                if i + 1 < m:
                    down = max(1, matrix[i+1][j]-dungeon[i][j])
                right = None
                if j + 1 < n:
                    right = max(1, matrix[i][j+1]-dungeon[i][j])
                if down and right:
                    matrix[i][j] = min(down, right)
                elif down:
                    matrix[i][j] = down
                elif right:
                    matrix[i][j] = right
        return matrix[0][0]

x = Solution()
print x.calculateMinimumHP([[0, 0]])