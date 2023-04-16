class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        power = pow(x,n/2)
        if n%2==0:
            return power*power
        else:
            return power*power*x
                