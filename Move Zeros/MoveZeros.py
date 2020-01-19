class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums)-1
        '''
        while(nums[j] == 0):
            j -= 1
        for i in range(j):
            if(nums[i]==0):
                x = i
                while(x<j):
                    nums[x] = nums[x+1]
                nums[j] = 0
                j -= 1
        '''
        '''
        while(i <= j):
            print (i)
            if(nums[i] == 0):
                nums.remove(nums[i])
                nums.append(0)
                j -= 1
            else:
                i += 1
                
        '''
            
        ind = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[ind] = nums[ind], nums[i]
                ind+=1