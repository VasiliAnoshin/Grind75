from string import ascii_lowercase
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if beginWord in wordSet:
            wordSet.remove(beginWord)
        
        
        def neighbors(word):
            for i in range(len(word)):
                for j in ascii_lowercase:
                    tmp = word[:i] + j + word[i+1:]
                    if tmp in wordSet:
                        yield tmp
        
        ans = 0
        q = deque([beginWord])
        while q:
            ans += 1
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == endWord:
                    return ans

                for newStr in neighbors(cur):
                    q.append(newStr)
                    wordSet.remove(newStr)
                    
        return 0  # no such transformation sequence.



if __name__ == "__main__":
    sol = Solution()
    sol.ladderLength("hot","dog",["hot","dog"])