class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # set two pointer, one goes 1 step, and the other goes 2 step
        s = f = head
        while f and f.next:
            f = f.next.next
            s = s.next
            if f == s:
                return True
        return False