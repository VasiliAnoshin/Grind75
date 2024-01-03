class Solution:

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

sol = Solution()
sol.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]])
sol.findMinHeightTrees(4, [[1,0],[1,2],[1,3]])