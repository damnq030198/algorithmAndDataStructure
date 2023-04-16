class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==1 or x==0:
            return x
        l=1
        r=x
        while l < r:
            mid = l+(r-l+1)/2
            if mid <= x/mid:
                l = mid
            else:
                r = mid-1
        return l
            