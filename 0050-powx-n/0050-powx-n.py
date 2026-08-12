class Solution(object):
    def power(self, x, n):

        if n == 0:
            return 1

        if n == 1:
            return x

        if n%2 == 0:
            return self.power(x*x, n/2)

        if n%2 != 0:
            return x*self.power(x, n-1)
        
    def myPow(self, x, n):

        if n<0:
            return 1 / self.power(x, -n)

        else:
            return self.power(x, n)

        