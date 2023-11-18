# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n==1:
            return 1
        i,j = 0, n
        while i < j:
            middle = (i + j)//2
            res = isBadVersion(middle)
            if not res:
                i = (middle +1)
            elif res and (middle-1>0) and isBadVersion(middle-1):
                j = middle-1
            else:
                return middle
        return j
                