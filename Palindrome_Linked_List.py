# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        store = []
        
        while head != None:
            store.append(head.val)
            head = head.next
        
        j = len(store)
        for i in range(0,(len(store)//2)):
            if store[i]!=store[j-1]:
                return 0
            j-=1
        return 1    
