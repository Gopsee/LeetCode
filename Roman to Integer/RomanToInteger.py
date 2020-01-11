class Solution:
    def romanToInt(self, s: str) -> int:
        table={
                "I":1,
                "V":5,
                "X":10,
                "L":50,
                "C":100,
                "D":500,
                "M":1000
                }
        res = table[s[-1]]
        n = len(s)
        for i in range(n-1):
            if table[s[i]] < table[s[i+1]]:
                res -= table[s[i]]
            else:
                res += table[s[i]]
        return res 
        