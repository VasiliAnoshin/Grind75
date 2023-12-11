### [Simple Solution](/String/atoi/basic_sol.py): math

```python
    def myAtoi(self, s: str) -> int:
        s= s.strip()
        if not s:
            return 0
        sign = 1 
        if s[0] in ("-","+"):
            sign = 1 if s[0] == "+" else -1
            s=s[1:]
        i = res = 0
        while i < len(s) and s[i].isdigit():
            res= res * 10 + int(s[i])
            i+=1
        res = sign * res
        return max(-2**31, min(res, 2**31-1))
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)