class Solution:
    def firstBadVersion(self, n: int) -> int:
        h = 1
        t = n
        while 1:
            if ((t-h)<=1) and not isBadVersion(h):
                return t
            elif ((t-h)<=1) and isBadVersion(h):
                return h            
            elif isBadVersion((h + t)//2):
                t = (h + t)//2
            elif not isBadVersion(((h + t)//2)):
                h = (h + t)//2