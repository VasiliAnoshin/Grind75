# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
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