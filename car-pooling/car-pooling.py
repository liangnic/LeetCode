class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        tripGuide = [x for n, i, j in trips for x in [[i, n], [j, - n]]]
        
        for i,j in sorted(tripGuide):
            capacity -= j
            if capacity < 0:
                return False
        return True