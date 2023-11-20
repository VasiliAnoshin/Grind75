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
                    while nums[l] == nums[l-1] and l<r:       #After sum was added add case for elimante duplicates. 
                        l+=1 
            i+=1
        return res
```

Time Complexity: ![O(n^2)](<https://latex.codecogs.com/svg.image?\inline&space;O(n^2)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)
# Three Sum Algorithm

## Explanation

The goal of this algorithm is to find triplets in an array that sum to zero while avoiding duplicates. Let's illustrate this with an example using the array `[-3, 3, 4, -3, 1, 2]`.

In this sequence, the triplet `[-3, 1, 2]` occurs twice, leading to a sum of zero:

```plaintext
-3 + 1 + 2 = 0

[-3, 3, 4, -3, 1, 2]
  ^         ^  ^  ^

The problem that we do no need the same number in  -3 + 1 + 2 =0 stay in first position twice.
                                                    ^
```
The solution to this problem is to sort inpout Array. Now we are looking at sorted array: `[-3, -3, 1, 2, 3, 4]`.
```plaintext
So now if we find this [-3, -3, 1, 2, 3, 4] three numbers. And then we have negative -3 again [-3, -3, 1, 2, 3, 4] that lead to duplicate.  
                         ^      ^  ^                                                                ^  ^  ^
And we know this because its left value is the same number we dont want to put twice. We continue to the next elm.
```

So after we find our first number. The we need to complete the remain two. 
And its lead us to 2sum problem based on two pointers where array is sorted.
And if we find two numbers that lead to sol we add to array. 
Else we shift pointers based on result. If sum > 0 then shift left right pointer. 
if sum < 0 shift right left pointer. 

There could be duplicates among the right and left values.
```plaintext
 For Example [-3, -3, -1, -1, 2, 3, 4]. For the next round you will see again [-3, -3, -1, -1, 2, 3, 4] That lead to 0. 
                                                                                ^       ^            ^    
```
