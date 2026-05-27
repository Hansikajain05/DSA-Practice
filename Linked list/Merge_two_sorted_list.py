class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):

        nums = []

        while list1:
            nums.append(list1.val)
            list1 = list1.next

        while list2:
            nums.append(list2.val)
            list2 = list2.next

        nums.sort()

        dummy = ListNode(0)
        curr = dummy

        for num in nums:
            curr.next = ListNode(num)
            curr = curr.next

        return dummy.next