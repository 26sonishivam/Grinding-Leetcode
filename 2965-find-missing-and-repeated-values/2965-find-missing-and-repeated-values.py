class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        
        n = len(grid)
        size = n*n

        hash = [0]*(size + 1)

        for i in range(n):
            for j in range(n):
                hash[grid[i][j]] += 1

        duplicate, missing = -1, -1

        for k in range(1, size+1):
            if hash[k] == 0:
                missing = k
            if hash[k] == 2:
                duplicate = k

        return [duplicate, missing]


