### [Improved Solution](/Stack/valid_parenthesis/basic_sol.py): Hash Table

```python
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
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

Explanation: Instead of searching the whole array blindlessly in each iteration, using a hash table can determine whether this element is the target value in ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>) time.