class Solution:
    def mySqrt(self, x: int) -> int:
        lo = 0
        hi = x//2
        if(x == 0):
            return 0
        if(x <= 3):
            return 1
        if(x == 5):
            return 2
        if(hi**2 == x):
            return hi
        while (True):
            if(hi- lo == 1):
                return lo
            mid = (lo+hi)//2
            if(mid**2 == x):
                return mid
            if(mid**2 > x):
                hi = mid
            if(mid**2 < x):
                lo = mid