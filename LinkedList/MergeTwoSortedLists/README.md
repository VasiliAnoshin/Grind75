### [Simple Solution](/LinkedList/MergeTwoSortedLists/basic_sol.py): Merge

```python
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        
        output = res = ListNode(0)
        while list1 and list2:
            if list1.val <= list2.val:
                output.next = list1
                list1 = list1.next
            else:
                output.next = list2
                list2 = list2.next
            output = output.next
        if not list1 or not list2:
            output.next = list2 if not list1 else list1
        return res.next
```

Time Complexity: ![O(m+n)](<https://latex.codecogs.com/svg.image?\inline&space;O(m+n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

### [Recursive Solution](/LinkedList/MergeTwoSortedLists/recursive_sol.py): Recursion

```python
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
```

Time Complexity: ![O(m+n)](<https://latex.codecogs.com/svg.image?\inline&space;O(m+n)>),
Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

Recursive Call Stack: Each recursive call to self.mergeTwoLists adds a new frame to the call stack. 
The space required on the call stack is proportional to the depth of the recursion, which is the sum of the lengths of the input lists.

In the worst case, the maximum depth of the call stack is m + n, where m is the length of list1 and n is the length of list2.
Each call frame contains local variables and control information.
Overall: The dominant factor in the space complexity is the recursive call stack. 
The space complexity is O(m + n) because the space required on the call stack is proportional to the sum of the lengths of the input lists.