class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        
        return head

def create_linked_list(lst):
    dummy = ListNode()
    tail = dummy
    for num in lst:
        tail.next = ListNode(num)
        tail = tail.next
    return dummy.next

def print_linked_list(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    print(lst)

head = create_linked_list([1, 1, 2])
solution = Solution()
new_head = solution.deleteDuplicates(head)
print_linked_list(new_head)  

head = create_linked_list([1, 1, 2, 3, 3])
new_head = solution.deleteDuplicates(head)
print_linked_list(new_head) 
