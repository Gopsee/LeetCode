class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int *ptr = &val;
         if(nums.size()==0) return 0;
        int l=0;
        int c=-1;
        for(int i=0; i<nums.size() ; i++)
        {
            if(c==-1 && nums[i]==val)
            {
                c=i;
            }
            if(c!=-1 && nums[i]!=val)
            {
                nums[c]=nums[i];
                nums[i]=val;
                i=c;
                c=-1;
            }
            if(nums[i]!=val)
            {
                l++;
            }
            
        }
        return l;
    }
};