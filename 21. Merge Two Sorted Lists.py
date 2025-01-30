class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2

        return dummy.next

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

list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])

solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)

print_linked_list(merged_list)
