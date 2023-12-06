
### [Simple Solution](/Array/MergeIntervals/basic_sol.py):
Problem: [here](https://leetcode.com/problems/merge-intervals/)!


```python
def merge(self, intervals):
    cur = []
    intervals = sorted(intervals, key=lambda x: x[0])
    for intr in intervals:
        if not cur:
            cur.append(intr)
        else:
            if cur[-1][1] >= intr[0]:
                x,y = cur.pop()
                cur.append([x, max(y, intr[1])])
            else:
                cur.append(intr)
    return cur
```
