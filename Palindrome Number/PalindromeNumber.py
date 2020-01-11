class Solution:
    def isPalindrome(self, x: int) -> bool:
        i=0
        j= (len(str(x))-1)
        strx = str(x)
        
        while(i<=j):
            if(i == j):
                return True
            if(strx[i]!=strx[j]):
                return False
            i += 1
            j -= 1
        return True