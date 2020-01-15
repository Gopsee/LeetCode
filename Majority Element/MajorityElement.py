class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 1
        #nums1 = [0*_ for _ in range(len(nums)+1)]
        #nums1 = nums.sort()
        nums.sort()
        for i in range(len(nums)):
            if(nums[i] == nums[i-1]):
                counter += 1
                print (counter)
                if(counter > (len(nums)/2)):
                    return nums[i]
        
        
        