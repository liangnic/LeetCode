class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        @lru_cache(None)
        def getCherries(row, c1, c2):
            
            if row == m:
                return 0
            
            cherries = grid[row][c1] if c1 == c2 else grid[row][c1] + grid[row][c2]
            
            ans = 0
            for i in range(c1-1, c1+2):
                for j in range(c2-1, c2+2):
                    if 0 <= i < n and 0 <= j < n :
                        ans = max(ans, getCherries(row+1, i, j))
            return ans + cherries
        
        return getCherries(0,0,n-1)
        