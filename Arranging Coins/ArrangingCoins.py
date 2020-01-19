class Solution:
    def arrangeCoins(self, n: int) -> int:
        new = 0
        k = 0
        while (new <= n):
            k += 1
            new =new +k
        return k-1
        