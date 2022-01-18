class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for x,y in enumerate(flowerbed):
            if (x == len(flowerbed)-1 or not flowerbed[x+1]) and (not y and (x == 0 or not flowerbed[x-1])):
                n -= 1
                flowerbed[x] = 1
                
                if n <= 0:
                    return True
        
        return not n