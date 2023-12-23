### [Simple Solution](/Array/FindAllAnagramsInString/basic_sol.py): Using sort

```python
    def findAnagrams(self, s: str, p: str):
        k,j = 0, len(p)
        output = []
        p = sorted(p)
        for i in range(j, len(s)+1):
            if p == sorted(s[k:i]):
                output.append(i-j)
            k+=1
        return output
```

Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)