# Sol 1:
class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash_set = set(s)
        max_length = 0
        if len(hash_set) == 1:
            return len(s)
        for i in hash_set:
            max_length += s.count(i)//2*2
        if max_length < len(s):
            return max_length + 1
        return max_length