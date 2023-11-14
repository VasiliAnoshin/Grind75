### [Improved Solution](/Array/TwoSum/basic_sol.py): Hash Table

```python
    seen = {}
    for i in range(len(nums)):
        val = target - nums[i]
        if val in seen: 
            return [i, seen[val]]
        else:
            seen[nums[i]] = i
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

Explanation: Instead of searching the whole array blindlessly in each iteration, using a hash table can determine whether this element is the target value in ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>) time.