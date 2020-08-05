First Soluntion using a dictionary and checking if the node already exists

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        dic = {}
        
        while head != None:
            if head in dic:
                return 1
            else:
                dic[head] = 0
                head = head.next    
        return 0   

Second solution using 2 pointer- one is slow and other pointer is fast

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        p1=p2=head
        
        while p2!=None and p2.next!=None :
            p2 = p2.next.next
            p1 = p1.next
            if p1 == p2:
                return 1
        return 0 
