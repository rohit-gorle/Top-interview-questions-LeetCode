# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        i = 1
        j = 1
        temp = head
        temp2 = head 
    
        while temp.next != None:
            temp = temp.next
            i += 1
        if i==1:
            return None 
        if i==n:
            temp2.val = temp2.next.val
            temp2.next = temp2.next.next
            return head
        while j+n <i:
            temp2 = temp2.next
            j += 1
            
         
        temp2.next = temp2.next.next
       
        return head
