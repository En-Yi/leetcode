class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = [] # 存目前最長的子字串
        record = '' # 存所有子字串中最長的部分
        for i in s:
            if i not in longest_substring: # 沒出現過的加入
                longest_substring.append(i)
            else:                
                # 如果出現更長的則替換 record
                if len(record) < len(longest_substring):
                    record = ''.join(longest_substring)
                # 替換目前最長的子字串
                longest_substring = longest_substring[longest_substring.index(i)+1::]
                longest_substring.append(i)
        return max(len(record), len(longest_substring))