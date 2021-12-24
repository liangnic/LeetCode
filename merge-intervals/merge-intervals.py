class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        ans = [intervals[0]]
        l,r = 1,0
        
        while l < len(intervals):
            if ans[r][1] < intervals[l][0]:
                ans.append(intervals[l])
                l += 1
                r += 1
            else:
                ans[r][1] = max(ans[r][1],intervals[l][1])
                l += 1
            
        return ans
            