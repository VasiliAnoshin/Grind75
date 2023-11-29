### [Simple Solution](/Graph/NumberOfIslands/basic_sol.py): Matrix

```python
from collections import deque
class Solution:
    def numIslands(self, grid) -> int:
        visited, num_islands = set(), 0
        rows = len(grid)
        cols = len(grid[0])
        def bfs(x, y, grid):
            q = deque()
            q.append((x,y))
            visited.add((x, y))
            
            while q:
                x, y = q.popleft()
                directions = [(0,1), (1,0), (-1,0), (0,-1)]
                for r,c in directions:
                    if (r+x in range(rows) and 
                        c+y in range(cols) and 
                        grid[r+x][c+y] == '1' and 
                        (r+x, c+y) not in visited):
                            q.append((r+x,c+y))
                            visited.add((r+x,c+y))
            
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1' and (x,y) not in visited:
                    bfs(x,y,grid)
                    num_islands += 1
        return num_islands
```

Time Complexity: ![O(N)](<https://latex.codecogs.com/svg.image?\inline&space;O(N)>), 
Space Complexity: ![O(N)](<https://latex.codecogs.com/svg.image?\inline&space;O(N)>)


### [Recursive Solution](/Graph/NumberOfIslands/recursive_sol.py):
``` python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols, number_of_islands = len(grid), len(grid[0]), 0 
        def dfs(row, column) -> None:
            exceed_boundaries = row not in range(rows) or column not in range(cols)
            if exceed_boundaries or grid[row][column] == "0":
                return

            grid[row][column] = "0"
            dfs(row-1, column)
            dfs(row+1, column)
            dfs(row, column-1)
            dfs(row, column+1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    number_of_islands += 1

        return number_of_islands
```
Explanation: Everytime we find a land ("1"), we perform DFS (depth-first search) to find all of the land in this island and change it to water ("0") so that we will not count it again in further iterations. After DFS, we have fully explored this particular island. Notice that it is feasible to change it to another character whatever you like except "1".
