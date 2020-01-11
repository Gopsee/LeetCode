class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return 1
        j = 0
        
        for i in range(len(nums)):
            if(nums[i-1] != nums[i]):
                nums[j] = nums[i]
                j += 1
            if(j == 0):
                return 1
            
        
        return j
    
        