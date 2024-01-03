### [Basic Solution](/BinaryTree/FindMinHeightTree/basic_sol.py): Binary Tree

**DFS:** 

```python
def findMinHeightTrees(self, n: int, edges):
        if n == 1:
            return [0]

        output = defaultdict(list)
        matrix = [[] for _ in range(n)]
        cache = {}

        for e1, e2 in edges:
            matrix[e1].append(e2)
            matrix[e2].append(e1)

        def dfs(node, parent, height, visited):
            if (node, parent) in cache:
                return cache[(node, parent)] + height
            max_height = height
            for child in matrix[node]:
                if child != parent and child not in visited:
                    visited.add(child)
                    res = dfs(child, node, height + 1, visited)
                    max_height = max(max_height, res)
            cache[(node, parent)] = max_height - height
            return max_height

        for i in range(n):
            visited = set()
            height = dfs(i, None, 0, visited)
            output[height].append(i)

        return output[min(output.keys())]
```

Explanation: For each node in the tree we trying to find the height. Result saving in Dict. 
At the end loioking for the nodes with min_height
Time Complexity: ![O(n^2)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n^2)](<https://latex.codecogs.com/svg.image?\inline&space;O(n^2)>)

### [Basic Solution](/BinaryTree/FindMinHeightTree/sol.py): Top.sort
```python
    def findMinHeightTrees(self, n: int, edges):
        if n == 1:
            return [0]

        mtx = [set() for _ in range(n)]
        for val1, val2 in edges:
            mtx[val1].add(val2)
            mtx[val2].add(val1)
        
        leaves = [i for i in range(n) if len(mtx[i]) == 1]
        
        while n>2:
            n-= len(leaves)
            new_leaves = []
            for i in leaves:
                val = mtx[i].pop()
                mtx[val].remove(i)
                if len(mtx[val]) == 1:
                    new_leaves.append(val)
            leaves = new_leaves
        return leaves

```

Explanation: 
First let's review some statement for tree in graph theory:

(1) A tree is an undirected graph in which any two vertices are
connected by exactly one path.

(2) Any connected graph who has n nodes with n-1 edges is a tree.

(3) The degree of a vertex of a graph is the number of
edges incident to the vertex.

(4) A leaf is a vertex of degree 1. An internal vertex is a vertex of
degree at least 2.

(5) A path graph is a tree with two or more vertices that is not
branched at all.

(6) A tree is called a rooted tree if one vertex has been designated
the root.

(7) The height of a rooted tree is the number of edges on the longest
downward path between root and a leaf.

OK. Let's stop here and look at our problem.

Our problem want us to find the minimum height trees and return their root labels. First we can think about a simple case -- a path graph.

For a path graph of n nodes, find the minimum height trees is trivial. Just designate the middle point(s) as roots.

Despite its triviality, let design a algorithm to find them.

Suppose we don't know n, nor do we have random access of the nodes. We have to traversal. It is very easy to get the idea of two pointers. One from each end and move at the same speed. When they meet or they are one step away, (depends on the parity of n), we have the roots we want.

This gives us a lot of useful ideas to crack our real problem.

For a tree we can do some thing similar. We start from every end, by end we mean vertex of degree 1 (aka leaves). We let the pointers move the same speed. When two pointers meet, we keep only one of them, until the last two pointers meet or one step away we then find the roots.

It is easy to see that the last two pointers are from the two ends of the longest path in the graph.

The actual implementation is similar to the BFS topological sort. Remove the leaves, update the degrees of inner vertexes. Then remove the new leaves. Doing so level by level until there are 2 or 1 nodes left. What's left is our answer!

The time complexity and space complexity are both O(n).

Note that for a tree we always have V = n, E = n-1.