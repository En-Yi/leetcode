class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:  
        # define dummy: follow temp,and increase nodes. temp: current pointer 
        dummy = temp = ListNode(0)
        # while list1, 2 both have nodes remaining
        while l1 != None and l2 != None: 
            if l1.val < l2.val: 
                temp.next = l1 # point to list1
                l1 = l1.next # jump to next node of list1
            else: 
                temp.next = l2 # point to list2
                l2 = l2.next # jump to next node of list2
            temp = temp.next # temp also point to next one

        # If one of list doesn't have any remaining node, then temp point to the other
        temp.next = l1 or l2

        # # Since the first is with value 0 (ListNode(0)),
        #  return dummy.next to exclude the first node
        return dummy.next