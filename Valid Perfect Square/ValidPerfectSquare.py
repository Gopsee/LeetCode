class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo = 0
        hi = num//2
        if (num == 1):
            return True
        if (num == 4):
            return 2
        
        while(lo<= hi):
            mid = (lo+hi)//2
            if(mid**2 == num):
                return True
            elif(mid**2 > num):
                hi = mid-1
            else:
                lo =mid +1
                
        return False 