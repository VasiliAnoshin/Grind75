### [Basic Solution](/BinaryTree/SerializeAndDeserializeBinaryTree/basic_sol.py): Binary Tree

```python
from collections import defaultdict
class Codec:
    def serialize(self, root):
        def dfs(root):
            if not root:
                res.append("None,")
                return 
            res.append(str(root.val)+",")
            dfs(root.left)
            dfs(root.right)
        res = []
        dfs(root)
        return "".join(res)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        def dfs(data):
            if not data or data[0] == 'None':
                data.pop(0)
                return None
            node = TreeNode(data.pop(0))
            node.left = dfs(data)
            node.right = dfs(data)
            return node
            
        output = dfs(data.split(','))
        return output
```
Explanation: 
