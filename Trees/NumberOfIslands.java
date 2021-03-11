package Leetcode;
/* 1. Idea is we are going to do a simple linear traversal through the matrix.
2. Whenever we come across "land" which is a '1' char, we are going to increment our land counter and we are going to get "rid" of the land.
3. So we want to "get rid of" the land because there may be multiple islands which are not connected, hence we need to visit those islands and increment our counter!
4. Now it is actually quite a simple process to get "rid of the land", all we do is a simple DFS recursive call once we find our first 1 in the linear traversal.
5. The dfs recursion will visit the top, bottom, left, right elements in the matrix respectively and transform them into 0's, and we know that 0 = water = our linear traversal will not halt on it.
6. Thus thats it! Not to bad at all, just traverse, find the land, remove the land with top-bottom-left-right dfs, move onto next land, repeat until matrix finished.
Time complexity: O(M * N) because of the matrix traversal
Space complexity: O(n) if all elements are '1' in the matrix for the call stack
 */
public class NumberOfIslands {
        public int numIslands(char[][] grid) {
        int islands = 0;
        for (int row = 0; row < grid.length; row++) {
            for (int col = 0; col < grid[row].length; col++) {
                if (grid[row][col] == '1') {
                    dfs(grid, row, col);
                    islands++;
                }
            }
        } return islands;
    }
    private void dfs(char[][] grid, int row, int col) {
        if (row >= 0 && col >= 0 && row < grid.length && col < grid[row].length && grid[row][col] == '1') {
            grid[row][col] = '0';
            dfs(grid, row - 1, col);
            dfs(grid, row + 1, col);
            dfs(grid, row, col - 1);
            dfs(grid, row, col + 1);
        }
    }
}
}
