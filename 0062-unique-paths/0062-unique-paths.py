class Solution:
    def uniquePaths(self, m, n):
        
        memo = {}
        
        def countPaths(row, col):
            
            if row > m-1 or col > n-1: 
                return 0

            if row == m-1 and col == n-1:
                return 1

            if (row, col) in memo:
                return memo[(row, col)]
            
            memo[(row, col)] = countPaths(row, col + 1) + countPaths(row + 1, col)
            return memo[(row, col)]

        return countPaths(0, 0)