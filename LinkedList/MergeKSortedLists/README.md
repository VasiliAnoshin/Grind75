### [Simple Solution](/LinkedList/MergeKSortedLists/basic_sol.py): MergeKSortedLists

```python
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        ll = lists[0]
        j, n = 1, len(lists)
        def merge(root1, root2):
            runner = head = ListNode()
            while root1 and root2:
                if root1.val > root2.val:
                    runner.next = root2
                    root2 = root2.next
                    runner = runner.next 
                else:
                    runner.next = root1
                    root1 = root1.next
                    runner = runner.next
            if root1 or root2:
                runner.next = root1 if root1 else root2
            return head.next
            
                
        while j < n:
            if lists[j]:    
                ll = merge(ll, lists[j])
            j+=1
        return ll
```

Explanation: 
Select 2 lists merge between them. And continue to next list.


Solution using HEAP.
```python
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda self, other: self.val < other.val
        h = []
        head = tail = ListNode(0)
        for i in lists:
            if i: heapq.heappush(h, i)
        while h:
            node = heapq.heappop(h)
            tail.next = node
            tail = tail.next
            if node.next: heapq.heappush(h, node.next)
        return head.next  
```