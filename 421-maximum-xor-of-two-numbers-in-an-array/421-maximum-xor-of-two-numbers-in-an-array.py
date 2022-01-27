class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        for i in reversed(range(32)):
            ans <<= 1
            prefixes = {num >> i for num in nums}
            ans += any(ans^1 ^ p in prefixes for p in prefixes)
        return ans
                    