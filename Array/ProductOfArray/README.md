
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
But you can't use division.

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
##### Calculate Final Output:
For each element at index i, multiply the corresponding values from the prefix and postfix arrays to get the product of all elements except the one at index i.

### Smart solution:
```python
    def productExceptSelf(self, nums):
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
```
## Initialization:
- res: The res array is initialized as an array of ones, representing the initial product. It will eventually store the product of all elements except the one at the current index.

## Calculate Prefix Products:
- Iterate through the array from left to right.
- For each element at index i, set the corresponding element in res to the product of all elements to the left of i.
- Update a variable prefix to represent the product of all elements to the left of the current index.

## Calculate Postfix Products:
- Iterate through the array from right to left.
- For each element at index i, multiply the current value in res by the product of all elements to the right of i.
- Update a variable postfix to represent the product of all elements to the right of the current index.
