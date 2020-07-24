class Solution:
    def numIslands(self, grid):
        numIslands = 0
        for i in range(0, len(grid)):
            for j in range (0, len(grid[0])):
                coord = str(i) + "," + str(j)
                if grid[i][j] == "1":
                    numIslands += 1
                    self.dfs(i,j,grid)
        return numIslands
                        
    def dfs (self, i, j,grid):
        if ( i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j]== "0"): 
            return
        # print(i,j)
        grid[i][j] = "0"
        self.dfs(i + 1, j,grid)
        self.dfs(i - 1, j,grid)
        self.dfs(i, j + 1,grid)
        self.dfs(i, j - 1,grid)
        



mySolution = Solution()
print(mySolution.numIslands(
    [
  ["1","0","1","1","0"],
  ["0","1","0","1","0"],
  ["1","0","0","0","1"]
]
))