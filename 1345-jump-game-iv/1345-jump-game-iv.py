class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        n = len(arr)
        idx = defaultdict(list)
        for i, num in enumerate(arr):
            idx[num].append(i)
        
        visited = [False for _ in range(n)]
        que = [(0, 0)]
        visited[0] = True
        
        while que:
            i, step = que.pop(0)
            for j in (idx[arr[i]] + [i-1, i+1]):
                if 0 <= j < n and visited[j] == False:
                    if j == n - 1 : 
                        return step + 1
                    visited[j] = True
                    que.append( (j, step + 1) )
            idx[arr[i]] = []
        
        return 0
