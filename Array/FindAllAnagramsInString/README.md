### [Simple Solution](/Array/FindAllAnagramsInString/basic_sol.py): Using sort

```python
    def findAnagrams(self, s: str, p: str):
        k,j = 0, len(p)
        output = []
        p = sorted(p)
        for i in range(j, len(s)+1):
            if p == sorted(s[k:i]):
                output.append(i-j)
            k+=1
        return output
```

Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

improved soulution using dictionary aka Counter:
```python
  def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        pCounter = Counter(p)
        sCounter = Counter(s[:len(p)-1])
        for i in range(len(p)-1,len(s)):
            sCounter[s[i]] += 1   # include a new char in the window
            if sCounter == pCounter:    # This step is O(1), since there are at most 26 English letters 
                res.append(i-len(p)+1)   # append the starting index
            sCounter[s[i-len(p)+1]] -= 1   # decrease the count of oldest char in the window
            if sCounter[s[i-len(p)+1]] == 0:
                del sCounter[s[i-len(p)+1]]   # remove the count if it is 0
        return res
```

another version using two arrays:
```python
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lenS = len(s)
        lenP = len(p)
        
        if lenS < lenP:
            return []
        """
	To find the anagram of a string, the frquencies of each char of string should match to the resulting string.
	**Approach: Sliding Window**
		Define two arrays, used as hashmap, to store the frequencies of alphabets(a-z) of given string **s**
		and the chars present in window at any point of time.
	"""
        hashmapS = [0] * 26
        hashmapP = [0] * 26
        
        for ch in p:
            hashmapP[ord(ch) - ord('a')] += 1
        
        left = 0
        right = lenP - 1
        
	# Calculating the frequency for each char in initial window
        for ch in range(left, right+1):
            hashmapS[ord(s[ch]) - ord('a')] += 1
        
        output = []
        
        while right < lenS:
            # Whenever the window string becomes anagram of **s**, append the left index of window to output.
            if hashmapP == hashmapS:
                output.append(left)
	    # Slide the window by 1 position and check for anagram again.
            hashmapS[ord(s[left]) - ord('a')] -= 1
            left += 1
            right += 1
            if right < lenS:
                hashmapS[ord(s[right]) - ord('a')] += 1
        if hashmapP == hashmapS:
            output.append(left)
        
        return output
```
