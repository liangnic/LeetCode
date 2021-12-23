class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        clen = len(prerequisites)
        if clen == 0:
            # 没有课程，当然可以完成课程的学习
            return [i for i in range(numCourses)]

        inverse_adj = [set() for _ in range(numCourses)]
        for second, first in prerequisites:
            inverse_adj[second].add(first)

        visited = [0 for _ in range(numCourses)]

        res = []
        for i in range(numCourses):
            if self.dfs(i,inverse_adj, visited, res):
                return []
        return res
        
    def dfs(self, vertex, inverse_adj, visited, res):
        """
        注意：这个递归方法的返回值是返回是否有环
        :param vertex: 结点的索引
        :param inverse_adj: 逆邻接表，记录的是当前结点的前驱结点的集合
        :param visited: 记录了结点是否被访问过，2 表示当前正在 DFS 这个结点
        :return: 是否有环
        """

        if visited[vertex] == 2:
            return True
        
        if visited[vertex] == 1:
            return False
        
        visited[vertex] = 2 #正在访问
        
        for vet in inverse_adj[vertex]:
            # 如果没有环，就返回 False，
            # 执行以后，逆拓扑序列就存在 res 中
            if self.dfs(vet, inverse_adj, visited, res):
                return True
        
        visited[vertex] = 1
        res.append(vertex)
        return False
        
