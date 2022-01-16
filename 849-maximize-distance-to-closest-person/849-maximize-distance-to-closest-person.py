class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        res, last = 0, -1
        n = len(seats)
        for i in range(n):
            if seats[i]:
                res = max(res, i if last < 0 else (i - last) / 2)
                last = i
        return int(max(res, n - last - 1))