### [Basic Solution](/BinarySearch/FirstBadVersion/basic_sol.py): Binary Search

```python
    def firstBadVersion(self, n: int) -> int:
        i,j = 1, n
        while i <= j:
            mid = (i + j)//2
            if isBadVersion(mid):
                j = mid-1
            else:
                i=mid+1
        return i
```

Time Complexity: ![O(log_n)](<https://latex.codecogs.com/svg.image?\inline&space;O(log_n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

Explanation:Create two pointers i and j. And move them correspondently depending on bs algorithm.