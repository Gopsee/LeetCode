class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 1
        sum1 = 0
        sum2 = 0
        while(i <= len(nums)):
            sum1 += i
            sum2 += nums[i-1]
            i += 1
            
        return sum1-sum2