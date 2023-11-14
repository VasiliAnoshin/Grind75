class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_braces = set('({[')
        braces, stack = dict({')':'(', '}': '{', ']':'['}), []
        for brace in s:
            if brace in left_braces: 
                stack.append(brace)
            else:
                if stack and stack[-1] == braces[brace]:
                    stack.pop()
                else:
                    return False
        return not stack
            