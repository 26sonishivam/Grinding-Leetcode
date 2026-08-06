class Solution:

    def setZeroes(self, matrix):

        m = len(matrix)
        n = len(matrix[0])

        firstRowZero = False
        firstColZero = False

        for j in range(n):
            if matrix[0][j] == 0:
                firstRowZero = True

        for i in range(m):
            if matrix[i][0] == 0:
                firstColZero = True

        for i in range (1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1,m):
            for j in range(1,n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if firstRowZero == True:
            for j in range(n):
                matrix[0][j] = 0

        if firstColZero == True:
            for i in range(m):
                matrix[i][0] = 0

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
sol = Solution()
sol.setZeroes(matrix)
for row in matrix:
    print(row)