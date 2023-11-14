### [Simple Solution](/LinkedList/MergeTwoSortedLists/basic_sol.py): Merge

```python
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

Time Complexity: ![O(m+n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)