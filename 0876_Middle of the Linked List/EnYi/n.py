class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head2 = head        
        length = 1
        while head.next is not None:
            head = head.next
            length += 1
        for i in range(length//2):
            head2 = head2.next
        return head2