class Solution:
    def findAnagrams(self, s: str, p: str):
        k,j = 0, len(p)
        output = []
        p = sorted(p)
        for i in range(j, len(s)+1):
            if p == sorted(s[k:i]):
                output.append(i-j)
            k+=1
        return output