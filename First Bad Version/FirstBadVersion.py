# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo = 0
        hi = n
        
        if(n == 1):
            return 1
               
        while(lo <= hi):
            mid = (lo+hi)//2
            if(isBadVersion(mid)):
                hi = mid-1
            if( not isBadVersion(mid)):
                if(mid < n):
                    lo = mid +1
            
        return lo