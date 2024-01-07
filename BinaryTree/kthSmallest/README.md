### [Basic Solution](/BinaryTree/kthSmallest/basic_sol.py): INORDER traverse BST

Depth-First Search

```python
    def kthSmallest(self, root, k: int) -> int:
        res = []
        def dfs(root):
            if root:
                dfs(root.left)
                res.append(root.val)
                dfs(root.right)
        dfs(root)
        return res[k-1]
```
Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)
Explanation: Traverse binary tree and add elm into arr. At the end return elm at k pos.