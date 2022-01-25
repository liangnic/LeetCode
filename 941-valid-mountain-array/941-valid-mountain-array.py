class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i, j, k = 0, len(arr), len(arr)-1
        while i+1 < j and arr[i] < arr[i+1]:
            i += 1
        while k > 0 and arr[k] < arr[k-1]:
            k -= 1
        
        return 0 < i == k < j-1
            
        