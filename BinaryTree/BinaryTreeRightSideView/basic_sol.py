from collections import deque
class Solution:
    def rightSideView(self, root):
        level_set = set()
        output = deque()
        def dfs(root, level):
            if root:
                if level not in level_set:
                    output.append(root.val)
                    level_set.add(level)
                dfs(root.right, level+1)
                dfs(root.left, level+1)
        dfs(root, 0)
        return list(output)