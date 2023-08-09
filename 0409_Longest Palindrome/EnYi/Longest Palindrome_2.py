class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict_s = {}
        max_length = 0
        record = 0
        for i in s:
            if i not in dict_s.keys():
                dict_s[i] = 1                    
                record += 1
            else:
                dict_s[i] += 1
                if dict_s[i] % 2 == 0:
                    max_length += 2                    
                    record -= 1
                else:
                    record += 1
        if record > 0:
            max_length += 1                    
        return max_length