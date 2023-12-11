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
1) <b>Start with an Empty Group:</b> We put a zero  to represent an empty group,  which has a sum of zero.
2) <b>Divide the Task:</b> For each element in the current set dp, create a new set new_dp and add two values to it: one with the current element added and one without adding the current element.
3) <b>Combinations:</b> For each number, we look at all the sums we currently have in our set. We create some new sums by either adding the number to the current sums or leaving the current sums unchanged.
4) After going through all the numbers, we check if the sum we want (half of the total sum) was found. If it is, it means we found a way to split the numbers into two groups with equal sums, and we say "Yes!" Otherwise, we say "No.

