public class Solution {
    public int numIslands(char[][] grid) {
        int result = 0;

        int rows = grid.length;
        if (rows == 0) {
            return 0;
        }
        
        int cols = grid[0].length;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == '1') {
                    result += 1;
                    this.visit(grid, i, j);
                }
            }
        }
        return result;
    }
    
    public void visit(char[][] grid, int i, int j) {
        int rows = grid.length;
        int cols = grid[0].length;
        if (i < 0 || j < 0 || i > rows - 1 || j > cols - 1) {
            return;
        }
        
        if (grid[i][j] != '1') {
            return;
        }
        
        grid[i][j] = '2';
        visit(grid, i - 1, j);
        visit(grid, i + 1, j);
        visit(grid, i, j - 1);
        visit(grid, i, j + 1);
    }
}