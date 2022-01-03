class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        count = [0]*(1+n)
        for i,j in trust:
            count[i] -= 1
            count[j] += 1
            
        for i in range(1, 1+n):
            if count[i] == n-1:
                return i
        return -1
        