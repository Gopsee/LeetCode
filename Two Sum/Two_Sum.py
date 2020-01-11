class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        
        for i in range(length):
            needed = target - nums[i]
            for j in range(i+1, length):
                if(nums[j] == needed):
                    return i, j
        