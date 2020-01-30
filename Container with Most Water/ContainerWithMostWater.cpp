class Solution {
public:
    int maxArea(vector<int>& height) {
        int maxContain=0,left=0,right=height.size()-1;
        while(left<right)
        {
            int temp=(right-left)*min(height[left],height[right]);
            if(temp>maxContain)
                maxContain=temp;
            else
            {
                if(height[left]>height[right])
                    right--;
                else
                    left++;
            }
        }

        return maxContain;
    }
};

