from heapq import heappush, heappop
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        result = []
        temp = self
        while temp:
            result.append(str(temp.val))
            temp = temp.next
        return "->".join(result)

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        for i, node in enumerate(lists):
            if node:
                heappush(heap, (node.val, i, node))
        
        dummy = ListNode(0)
        current = dummy
        
        while heap:
            val, i, node = heappop(heap)
            current.next = node
            current = node
            
            if node.next:
                heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next
