class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if not nums:
            return 0
        if N == 1:
            return nums[0]
        if N == 2:
            return max(nums)

        dp = [0*_ for _ in range(N+1)]
        dp[1] = nums[0]
        dp[2] = nums[1]
        for i in range(2,N):
            max_so_far = max(dp[i-1],dp[i-2])
            dp[i+1] = max(dp[i], nums[i]+max_so_far)
        return dp[N]
        