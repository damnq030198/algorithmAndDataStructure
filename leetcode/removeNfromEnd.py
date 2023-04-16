# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length=0
        tmp =head
        while tmp:
            length+=1
            tmp =tmp.next
        if length == n:
            return head.next
        elif n>length:
            return head
        else:
            dif = length-n
            prev=None
            cur = head
            for i in range(dif):
                prev=cur
                cur =cur.next
            prev.next =cur.next
        return head