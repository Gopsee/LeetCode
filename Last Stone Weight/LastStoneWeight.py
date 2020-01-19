class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        i = 0
        j = len(stones)
               
        while(j-1>=1):
            stones = sorted(stones)
            diff = stones[j-1] -stones[j-2]
            if(diff== 0):
                stones[j-2] = 0
                j -= 1
                
            else:
                stones[j-2] = diff
                j -= 1
            
        return stones[0]
            