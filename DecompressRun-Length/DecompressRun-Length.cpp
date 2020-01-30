class Solution {
public:
    vector<int> decompressRLElist(vector<int>& nums) {
        vector<int> newlist;
        for(int i = 0; i+1<nums.size();i+=2){
            int a = nums[i];
            int b = nums[i+1];
            while(a>0){
                newlist.push_back(b);
                a--;
            }
        }
        return newlist;
    }
};
