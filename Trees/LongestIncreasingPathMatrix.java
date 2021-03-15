/* 1. Idea is we have a matrix and we want to find the longest increasing path in the matrix.
2. Approach this matrix as a directed graph. Each element of the matrix is a vertice.
3. The basic approach is simple. Take each individual element in the matrix and do a DFS search through the entire matrix with conditions that require the next value in the path to always be greater than the current.
4. As long as this recursion keeps going, we are adding to the path for the one specific element, at the end we just return the element with the maximum path in the matrix.
5. However, we MUST alter this algorithm to a degree as it is to expensive! We will use Memoization to make this algorithm more efficient. Check out this piece on Memoization below.

* Now if we use memoization the algorithm will be as follows.
1. Define a final variable DIRECTIONS which holds down, up, left, right indexes respectively. We will use with our DFS to build our path.
2. Define a memoization matrix which has dimensions m x n and is populated with all 0's. We will use this matrix, in particular, each element in this matrix will correspond to each element in the original matrix.
3. The way the memoization matrix and OG matrix correlate is that once we have done a DFS search throughout our entire matrix for any one element, we will set the value of the element at its corresponding index in the memoization matrix as the value of the maximum increasing path for that OG matrix element.
4. Therefore, we don't have to recompute the path every single time! We can simply do a check and see, hey is this 0? if it is then I haven't calculated it's path yet, if it isn't then I need to find the max path for this element, so I will go ahead and DFS.
5. At the end of that DFS i set that element to the maximum path it could have taken + 1 to account for it's own path as each element itself is counted as a valid path.
 */
package Leetcode;

public class LongestIncreasingPathMatrix {

    private int[][] DIRECTIONS = {{1, 0}, {-1, 0}, {0, -1}, {0, 1}};

    public int longestIncreasingPath(int[][] matrix) {
        if (matrix.length == 0 || matrix == null) return 0;
        int rows = matrix.length;
        int cols = matrix[0].length;
        int longestPath = 0;
        int[][] memoization = new int[rows][cols];
        for (int currRow = 0; currRow < rows; currRow++) {
            for (int currCol = 0; currCol < cols; currCol++) {
                int longest = dfs(matrix, memoization, rows, cols, currRow, currCol);
                longestPath = Math.max(longestPath, longest);
            }
        }
        return longestPath;
    }

    public int dfs(int[][] matrix, int[][] memoization, int rows, int cols, int currRow, int currCol) {
        if (memoization[currRow][currCol] != 0) return memoization[currRow][currCol];
        int max = 0;
        for (int[] direction : DIRECTIONS) {
            int X = direction[0] + currRow;
            int Y = direction[1] + currCol;
            if (X >= 0 && Y >= 0 && X < rows && Y < cols && matrix[X][Y] > matrix[currRow][currCol]) {
                int longest = dfs(matrix, memoization, rows, cols, X, Y);
                max = Math.max(max, longest);
            }
        }
        memoization[currRow][currCol] = max + 1;
        return memoization[currRow][currCol];
    }
}

