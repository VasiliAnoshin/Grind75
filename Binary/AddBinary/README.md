### [Basic Solution](/Binary/FirstBadVersion/basic_sol.py): Binary Search

```python
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
```

### [Improved Solution](/BinarySearch/FirstBadVersion/basic_sol.py):

```python
    def addBinary(self, a: str, b: str) -> str:
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
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(log_n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

Explanation:Create two pointers i and j. And move them correspondently depending on bs algorithm.