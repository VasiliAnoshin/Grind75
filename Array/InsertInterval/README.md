### [Simple Solution](/Array/InsertInterval/basic_sol.py): 

```python
def insert(intervals, newInterval):
    start, end, output = 0, 1, []
    for i, inter in enumerate(intervals):
        if inter[start] > newInterval[end]:
            output.append(newInterval)
            output.extend(intervals[i:])
            return output
        elif inter[end] < newInterval[start]:
            output.append(inter)
        else:
            newInterval[start] = min(newInterval[start], inter[start])
            newInterval[end] = max(newInterval[end], inter[end])
    output.append(newInterval)
    return output
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n^2)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)