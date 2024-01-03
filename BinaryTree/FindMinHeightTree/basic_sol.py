from collections import defaultdict
class Solution:
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