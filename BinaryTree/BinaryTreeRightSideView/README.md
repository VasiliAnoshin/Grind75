### [Basic Solution](/BinaryTree/BinaryTreeRightSideView/basic_sol.py): Binary Tree

Depth-First Search

```python
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        seen = set()
        output = deque()
        def dfs(root, level):
            if root:
                if level not in seen:
                    output.append(root.val)
                    seen.add(level)
                dfs(root.right, level+1)
                dfs(root.left, level+1)
        dfs(root, 0)
        return list(output)
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

- Init 2 new vars. One for output and one for deque. 
- Algorithm: Traverse the whole tree starting from the right side => check if current level in seen.
- If level in seen that mean righmost value was inserted. But we still need to check entire tree. 
- If level not in seen we need to append value of root to deque and add level to seen.