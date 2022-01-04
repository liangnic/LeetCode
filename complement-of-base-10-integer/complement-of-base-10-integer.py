class Solution:
    def bitwiseComplement(self, n: int) -> int:
        p = 2
        while p <= n:
            p *= 2
        
        return p - n - 1
        