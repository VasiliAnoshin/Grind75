
### [Simple Solution](/Array/ProductOfArray/basic_sol.py): Prefix Product & Suffix Product
Problem: [here](https://leetcode.com/problems/product-of-array-except-self)!

It is simple problem once using division. After calculate product 
You can iterate in result array and for current index divide it by value like this one: 
```python
    def productExceptSelf(self, nums):
        prefix, output = 1, [0]*len(nums)
        for i in range(len(nums)):
            prefix *= nums[i]
        for j in  range(len(nums)):
            output[j] = prefix//nums[j]
        return output
```
But you can use division.

```python
    def productExceptSelf(self, nums): 
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        #final output is 
        output = [1] * len(nums) 
        #calculate prefix
        for i in range(len(nums)):
            prefix[i] = nums[i] if i == 0 else nums[i] * prefix[i-1]
        #calculate postfix
        for i in range(len(nums)-1, -1, -1):
            postfix[i] = nums[i] if i == len(nums)-1 else nums[i] * postfix[i+1]
        #calculate output. 
        for i in range(len(nums)):
            if i -1 < 0:
                output[i] *= postfix[i+1]
            elif i+1>=len(nums):
                output[i] *= prefix[i-1]
            else:
                output[i] =  postfix[i+1] * prefix[i-1]
        return output
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)
Algorithm: Suppose our prefix: started [a,b,c,d] => [a, ab, abc, abcd]. Postfix: [d,c,b,a] => [abcd,abc,ab,a].



