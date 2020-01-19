class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = int(len(nums))
        if(target > nums[(hi-1)] or target < nums[lo]):
            return -1
        while(lo <= hi):
            mid = (lo+hi)//2
            if(nums[mid] == target):
                return mid
            if(nums[mid] < target):
                lo = mid +1
            if(nums[mid] > target):
                hi = mid - 1
        return -1
            