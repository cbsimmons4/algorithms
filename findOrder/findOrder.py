class Solution:

    def findOrder(self, numCourses, prerequisites):

        leafCandidates = set()

        graph = {}

        for prereq in prerequisites:
            leafCandidates.add(prereq[1])

            if (prereq[1] not in graph):
                graph[prereq[1]]= [prereq[0]]
            else:
                graph[prereq[1]].append(prereq[0])

        for prereq in prerequisites:
            if (prereq[0] in leafCandidates):
                leafCandidates.remove(prereq[0])

        Q = []
        for leaf in leafCandidates:
            Q.append(leaf)
        if (len(Q) == 0 and len(prerequisites) > 0): return []
        visited = []

        while len(Q) > 0:
            cur = Q[0]
            del Q[0]
            visited.append(cur)
            if cur in graph:
                for neighbor in graph[cur]:
                    if neighbor in visited:
                        print('oi bruv')
                        return []
                    else:
                        if neighbor not in Q:
                            Q.append(neighbor)
            
        for i in range(0,numCourses):
            if i not in visited:
                visited.append(i)

        return visited

mySolution = Solution()
print(mySolution.findOrder(2, [[0,1],[1,0]]))