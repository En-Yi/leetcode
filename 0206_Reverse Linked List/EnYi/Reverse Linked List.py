class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        # 多用一個變數去存現有的變數，一直交替
        while curr:
            a = curr.next
            curr.next = prev
            prev = curr
            curr = a
        return prev