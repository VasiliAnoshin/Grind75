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

improved soulution using dictionary aka Counter:
```python
  def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        pCounter = Counter(p)
        sCounter = Counter(s[:len(p)-1])
        for i in range(len(p)-1,len(s)):
            sCounter[s[i]] += 1   # include a new char in the window
            if sCounter == pCounter:    # This step is O(1), since there are at most 26 English letters 
                res.append(i-len(p)+1)   # append the starting index
            sCounter[s[i-len(p)+1]] -= 1   # decrease the count of oldest char in the window
            if sCounter[s[i-len(p)+1]] == 0:
                del sCounter[s[i-len(p)+1]]   # remove the count if it is 0
        return res
```