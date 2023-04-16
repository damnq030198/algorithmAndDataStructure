# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        mid = 0
        l = 0
        r = n
        while l<r:
            mid = l +(r-l)//2
            if not isBadVersion(mid):
                l = mid +1
            else :
                r = mid
        return l