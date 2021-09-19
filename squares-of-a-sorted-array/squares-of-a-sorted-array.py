class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = [0] * n
        
        x,y,pos = 0, n-1, n-1
        while x <= y:
            if nums[x]*nums[x] > nums[y]*nums[y]:
                ans[pos] = nums[x]*nums[x]
                x += 1
            else:
                ans[pos] = nums[y]*nums[y]
                y -= 1
            pos -= 1
        
        return ans
            
        