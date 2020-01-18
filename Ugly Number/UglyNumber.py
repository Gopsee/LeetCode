class Solution:
    def isUgly(self, num: int) -> bool:
        counter = 0
        
        
        while(counter < 100):
            if(num == 1):
                return True
            temp = num
            if(num%5 == 0):
                num = num//5
            if(num%3 == 0):
                num = num//3
            if(num%2 == 0):
                num = num//2
            
            if(num == temp):
                return False
            counter += 1