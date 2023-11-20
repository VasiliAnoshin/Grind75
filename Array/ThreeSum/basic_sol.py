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


if __name__ == "__main__":
    res = threeSum([-1,0,1,2,-1,-4])
    print(res)