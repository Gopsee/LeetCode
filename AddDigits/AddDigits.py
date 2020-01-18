class Solution:
    def addDigits(self, num: int) -> int:
        
        counter = 0
        while(counter < len(str(num))+1):
            summ = 0
            for x in (str(num)):
                summ += int(x)
                print(summ)
            num = summ
            counter += 1
                
              
        return summ