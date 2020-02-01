class Solution {
public:
    bool isPowerOfThree(int n) {
        if (n == 1) return true;
        else if (n < 3) return false;
        while (n%3 == 0){
            cout<<n;
            n /= 3;
        }
        return n == 1;
    }
};