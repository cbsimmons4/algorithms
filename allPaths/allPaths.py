class Solution:
    def allPathsSourceTarget(self, graph):
        self.paths = []
        self.allPathsSourceTargetHelper(graph, [], 0)
        return self.paths

    def allPathsSourceTargetHelper(self, graph, path, i):
        if i >= len(graph):
            return
        path.append(i)
        if i == len(graph) - 1:
            self.paths.append(path)
        else: 
            for j in graph[i]:
                self.allPathsSourceTargetHelper( graph, path[:], j)



mySolution = Solution()
print(mySolution.allPathsSourceTarget([[1,2], [3], [3], []]))