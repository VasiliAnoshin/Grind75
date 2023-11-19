### [Basic Solution](/Binary/AddBinary/basic_sol.py): Binary Search

```python
    def addBinary(self, a: str, b: str) -> str:
        a = [int(char) for char in a]
        b = [int(char) for char in b]
        carrie, res = 0, []
        while a or b or carrie: 
            val = 0 
            if a:
                val += a.pop()
            if b:
                val += b.pop()
            res.append((val + carrie)%2)
            carrie = 1 if (val + carrie) >= 2 else 0
        return "".join([str(num) for num in res[::-1]])
```

### [Improved Solution](/Binary/AddBinary/basic_sol.py): Binary Search

```python
    def addBinary(self, a: str, b: str) -> str:
        a = [int(char) for char in a]
        b = [int(char) for char in b]
        carrie, res = 0, []
        while a or b or carrie: 
            if a:
                carrie += a.pop()
            if b:
                carrie += b.pop()
            res.append(str(carrie%2))
            carrie //=2
        return "".join(res[::-1])
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(log_n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

Explanation: This algorithm is designed to add two binary strings and return the result as a binary string. It follows the principles of binary addition, where you start from the least significant bit (LSB) and move towards the most significant bit (MSB), carrying over when the sum exceeds 1
- ##### Perform Binary Addition: </br>
 A while loop is used to iterate through the bits of a and b, performing binary addition.
 The loop continues until there are no more bits in a or b, and there is no remaining carry (carrie is not zero).
- ##### Sum Bits and Update Carry: </br>
 Inside the loop, the code checks if there are bits remaining in a or b. If so, it adds the current bit to the carry.
 ```python
    if a:
        carrie += a.pop()
    if b:
        carrie += b.pop()
 ```
