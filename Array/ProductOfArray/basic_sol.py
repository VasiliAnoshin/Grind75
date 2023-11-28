import math
class Solution:
    def productExceptSelf(self, nums):
        #calculate prefix
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        output = [1] * len(nums)
        for i in range(len(nums)):
            prefix[i] = nums[i] if i == 0 else nums[i] * prefix[i-1]
        for i in range(len(nums)-1, -1, -1):
            postfix[i] = nums[i] if i == len(nums)-1 else nums[i] * postfix[i+1]
        for i in range(len(nums)):
            if i -1 < 0:
                output[i] *= postfix[i+1]
            elif i+1>=len(nums):
                output[i] *= prefix[i-1]
            else:
                output[i] =  postfix[i+1] * prefix[i-1]
        return output

            
if __name__ == "__main__":
    sol = Solution()
    li = [10, 20]
    li.extend('30')
    print(sol.productExceptSelf([1,2,3,4]))
    print(sol.productExceptSelf([-1,1,0,-3,3]))