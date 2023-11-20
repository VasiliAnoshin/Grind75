### [Simple Solution](/Array/ThreeSum/basic_sol.py): 

```python
    def threeSum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        i, r, res= 0,  len(nums), []
        while i < r:
            if i>0 and nums[i] == nums[i-1]:
                i+=1
                continue
            l = i + 1
            r = len(nums) -1
            while l<r:
                val = nums[i] + nums[l] + nums[r]
                if val < 0:
                    l+=1
                elif val > 0:
                    r-=1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
            i+=1
        return res
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)
Explanation: The idea behind this algorithm is to track the minimum price encountered so far (global_min) and calculate the profit that can be obtained by selling at the current price (prices[i]) minus the minimum price. The maximum profit is updated whenever a higher profit is found during the iteration.