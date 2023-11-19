class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = [int(char) for char in a]
        b = [int(char) for char in b]
        carrie, res = 0, []
        while a or b or carrie: 
            val = 0 
            if a:
                val += a.pop()
            if b:
                val += b.pop()
            res.append((val + carrie)%2)
            carrie = 1 if (val + carrie) >= 2 else 0
        return "".join([str(num) for num in res[::-1]])
    
    def shortSolution(self, a: str, b: str) -> str:
        a = [int(char) for char in a]
        b = [int(char) for char in b]
        carrie, res = 0, []
        while a or b or carrie: 
            if a:
                carrie += a.pop()
            if b:
                carrie += b.pop()
            res.append(str(carrie%2))
            carrie //=2
        return "".join(res[::-1])

if __name__ == "__main__":
    sol = Solution()
    sol = sol.shortSolution("1010", "1011")