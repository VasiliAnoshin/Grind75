class Solution:
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