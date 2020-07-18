class Solution:
    def networkDelayTime(self, times, N, K):
        sourceDist = {}
        adjList = {}
        visited = set()
        onNoticedDist = {}
        for edge in times:
            sourceDist[edge[0]] = float('inf')
            sourceDist[edge[1]] = float('inf')
            if edge[0] in adjList.keys():
                adjList[edge[0]].append([edge[1],edge[2]])
            else: 
                adjList[edge[0]] = [[edge[1], edge[2]]]
        sourceDist[K] = 0
        visited.add(K)
        visitedDist[0] = K
        return adjList
        while (len(visited) != len(sourceDist.keys())):
            cur = sorted(visited[sorted(visitedDist.keys())])
            for neighbor in adjList[cur]:
                if cur[]
            

        # return visited
        
mySolution = Solution()

print (mySolution.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]],4,2))