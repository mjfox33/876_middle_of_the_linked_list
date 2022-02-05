# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        arr = list()
        arr.append(head)
        if head.next == None:
            return head
        ln = head
        while 1:
            ln = ln.next
            if ln == None:
                break
            arr.append(ln)
        n = len(arr)
        return arr[n//2]