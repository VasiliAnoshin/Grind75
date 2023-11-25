### [Simple Solution](/Graph/cloneGraph/basic_sol.py): cloneGraph

```python
      def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def clone(node):
            if not node:
                return        
            new_node = Node(node.val, [])
            exist[node.val] = new_node
            for neighbor in node.neighbors:
                if neighbor.val not in exist:
                    clone(neighbor)
                exist[new_node.val].neighbors.append(exist[neighbor.val])
            return new_node
        exist = dict()
        return clone(node)
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(m+n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)



