# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        pre_result = ListNode(0)
        current = pre_result
        carry = 0

        while l1 is not None and l2 is not None:
            sum_val = l1.val + l2.val + carry
            current.next = ListNode(sum_val % 10)
            carry = sum_val / 10
            current = current.next
            l1 = l1.next
            l2 = l2.next

        l = l1 or l2

        while l is not None:
            sum_val = l.val + carry
            current.next = ListNode(sum_val % 10)
            carry = sum_val / 10
            current = current.next
            l = l.next

        if carry > 0:
            current.next = ListNode(carry)

        return pre_result.next
