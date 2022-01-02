class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        times = [0]*60
        
        ans = 0
        
        for i in time:
            if i%60 == 0:
                ans += times[0]
            else:
                ans += times[60-i%60]
            times[i%60] += 1
        
        return ans
        