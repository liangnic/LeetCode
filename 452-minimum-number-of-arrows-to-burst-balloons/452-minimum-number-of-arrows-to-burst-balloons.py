class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort(key=lambda p: p[1])
        
        ans, p = 0, 0
        
        for start, end in points:
            if ans == 0 or start > p:
                ans += 1
                p = end
        
        return ans