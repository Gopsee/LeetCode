class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sort = sorted(nums)
        if(len(sort)==1):
            return False
        for x in range(len(sort)):
            if(sort[x] == sort[x-1]):
                return True
        return False