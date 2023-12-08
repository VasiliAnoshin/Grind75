### [Basic Solution](/BinaryTree/LowestCommonAncestor/basic_sol.py): Binary Tree

Depth-First Search

```python
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        elif not left and not right:
            return None
        else:
            return left if left else right
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

- Tushar Roy: https://www.youtube.com/watch?v=13m9ZCB8gjw&ab_channel=TusharRoy-CodingMadeSimple