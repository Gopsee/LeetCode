class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict = list()
        arr = list()
        new = list()
        
        for i in nums1:
            if(i not in dict):
                dict.append(i)
        
        for j in nums2:
            if(j in dict):
                if(j not in arr):
                    arr.append(j)
                
        
        #if k not in arr:
         #   new.append(i)
        
        return arr