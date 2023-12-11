### [Basic Solution](/DynamicProgramming/SubsetSum/basic_sol.py):: DP

```python
    def canPartition(self, nums) -> bool:
        if sum(nums)%2!=0:
            return False
        dp = set()
        dp.add(0) # add first elm for start calculation. i.e [1.2.3.4] 0 +1. 0 +11. We need option to add elm itself to output.
        target = sum(nums)//2
        for num in nums: 
            new_dp = set() #we add new collection as we cant change collection that we are runnig on.
            for elm in dp: 
                new_dp.add(elm + num)
                new_dp.add(elm)
            dp = new_dp
        return True if target in dp else False 
```

Time Complexity: ![O(sum(nums))](<https://latex.codecogs.com/svg.image?\inline&space;O(sum(nums))>), Space Complexity: ![O(sum(nums))](<https://latex.codecogs.com/svg.image?\inline&space;O(sum(nums))>)

Explanation:
