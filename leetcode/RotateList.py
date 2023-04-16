# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
        tmp = head
        b = head
        s = head
        result = head
        length =0 
        while tmp :
            length +=1
            tmp = tmp.next
        k = k%length
        for i in range(k):
            b = b.next
        while b.next:
            b = b.next
            s = s.next
        b.next = head 
        result = s.next
        s.next = None
        return result