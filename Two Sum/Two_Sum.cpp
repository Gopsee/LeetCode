class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> indexs(2);
	for (int i = 0; i < nums.size(); i++) {
		for (int j = i+1; j < nums.size(); j++)
		if (nums[i] + nums[j] == target) {
			indexs[0] = j  ;
			indexs[1] = i ;
			return indexs;
		}
	}
	return indexs;
    }
};