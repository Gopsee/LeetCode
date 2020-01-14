class Solution {
public:
    int climbStairs(int n) {
        if(n ==1)
            return 1;
        int ones = 1;
        int twos = 2;
        for (int i=3; i<=n; i++){
            int total = ones + twos;
            ones = twos;
            twos = total;
        }
        return twos;
        
    }
};