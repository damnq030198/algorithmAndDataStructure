# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tmp = ListNode(0)
        l3=tmp
        carry=0
        while l1 or l2:
            s =0
            if l1:
                s+=l1.val
                l1 =l1.next
            if l2:
                s+=l2.val
                l2=l2.next
            s+=carry
            tmp.next=ListNode(s%10)
            tmp = tmp.next
            carry=s//10
        if carry==1:
            tmp.next=ListNode(carry)
        return l3.next