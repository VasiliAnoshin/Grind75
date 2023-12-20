### [Basic Solution](/BinaryTree/ConstructBinaryFromPreorder/basic_sol.py): Binary Tree

```python
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder  or not inorder:
            return None
        node = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        node.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        node.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return node
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

Explanation:
Explanation: To solve this problem, we have to use the properties of preorder and inorder traversal. We know that preorder traversal sequentially visits the root, left child, and right child. On the other hand, inorder traversal sequentially visits the left child, root, and right child. With this in mind, the root of the binary tree is the first element of the preorder traversal. For example, assume that the preorder traversla and inorder traversal of an arbitrary binary tree is [3, 9, 20, 15, 7] and [9, 3, 15, 20, 7], respectively. Then, we know that the root of that tree is 3. Since we know that the root node is 3, we can tell from the inorder traversal that elements located on the left hand side of 3 are the left subtree of the root node and elements located on the right hand side of 3 are the left subtree of the root node. In this case, 9 is in the left subtree of the root node, while [15, 20, 7] are in the right subtree of the root node. By doing so recursively, we can solve this problem.