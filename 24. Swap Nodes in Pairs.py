class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next
            
            prev.next = second
            first.next = second.next
            second.next = first
            
            prev = first
        
        return dummy.next

def list_to_linked_list(arr):
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

solution = Solution()

head = list_to_linked_list([1, 2, 3, 4])
print(linked_list_to_list(solution.swapPairs(head)))  # Output: [2, 1, 4, 3]

head = list_to_linked_list([])
print(linked_list_to_list(solution.swapPairs(head)))  # Output: []

head = list_to_linked_list([1])
print(linked_list_to_list(solution.swapPairs(head)))  # Output: [1]

head = list_to_linked_list([1, 2, 3])
print(linked_list_to_list(solution.swapPairs(head)))  # Output: [2, 1, 3]
