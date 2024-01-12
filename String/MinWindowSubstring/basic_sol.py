from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i = 0
        cnt_t, cnt_s = Counter(t), Counter()
        max_i, max_j = -float('inf'), float('inf')
        output = ''
        for j, val in enumerate(s):
            cnt_s[val] +=1
            while cnt_t & cnt_s == cnt_t:
                if j-i<max_j-max_i:
                    output = s[i:j+1]
                    max_j = j
                    max_i = i
                cnt_s[s[i]]-=1
                i+=1
        return '' if not output else output