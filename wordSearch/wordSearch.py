class Solution:
    def exist(self, board, word):
        graph = {}
        starts = []
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                key = str(i) + "," + str(j)
                graph[key] = []
                if board[i][j] == word[0]:
                    starts.append([i,j])
                if ((i - 1 >= 0) and (i - 1  < len(board)) and (j >= 0) and (j < len(board[0]))):
                    curVal = str(i-1) + "," + str(j)
                    graph[key].append(curVal)
                if ((i + 1 >= 0) and (i + 1  < len(board)) and (j >= 0) and (j < len(board[0]))):
                    curVal = str(i+1) + "," + str(j)
                    graph[key].append(curVal)
                if ((i >= 0) and (i < len(board)) and (j + 1 >= 0) and (j + 1 < len(board[0]))):
                    curVal = str(i) + "," + str(j + 1)
                    graph[key].append(curVal)
                if ((i >= 0) and (i < len(board)) and (j - 1 >= 0) and (j - 1 < len(board[0]))):
                    curVal = str(i) + "," + str(j - 1 )
                    graph[key].append(curVal)

        for start in starts:
            if self.dfs(start[0],start[1], 0, word, set(), graph, board): return True

        return False

    def dfs(self, i, j, k, word, visited, graph, board):
        if k >= len(word):
            return True
        if (  i < 0  or  i >= len(board) or j < 0  or j >= len(board[0]) or (str(i) + "," + str(j)) in visited or board[i][j] != word[k]):
            return False
        if k == len(word) - 1 and word[k] == board[i][j] and (str(i) + "," + str(j)) not in visited:
            return True
        key = str(i) + "," + str(j)
        visited.add(key)
        for neighbor in graph[key]:
            nextIndexArray = neighbor.split(',')
            if self.dfs(int(nextIndexArray[0]), int(nextIndexArray[1]), k + 1, word, visited, graph, board):
                return True
        visited.remove(key)
        return False




mySolution = Solution()
print(mySolution.exist(
    [
  ["a"]
],
"a"
))