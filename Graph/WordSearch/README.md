### [Simple Solution](/Graph/WordSearch/basic_sol.py): Graph

```python
def exist(self, board: list[list[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        rows, cols = len(board), len(board[0])

        def dfs(x, y, index):
            if index == len(word):
                return True

            if (x in range(rows) and y in range(cols)
                and board[x][y] == word[index]):
                temp, board[x][y] = board[x][y], '/'
                if (
                    dfs(x + 1, y, index + 1)
                    or dfs(x - 1, y, index + 1)
                    or dfs(x, y + 1, index + 1)
                    or dfs(x, y - 1, index + 1)
                ):
                    return True
                board[x][y] = temp

            return False

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False
```

Time Complexity: ![O(4^n^2)](<https://latex.codecogs.com/svg.image?\inline&space;O(4^n^2)>), 
Explanation: loop for all chars in matrix and ru DFS that check if there exist at least one path that lead to to provided path. 
This is not optimal solution since it path over all existing chars and trying to look in all directions.
In each step: we remove the same char and put '/' insted. To understand that we were here before. 

