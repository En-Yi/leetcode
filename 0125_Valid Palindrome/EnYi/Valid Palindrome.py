class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for char in s:
            if char.isalnum():
                result += char
        result = result.lower()
        
        i = 0
        while (i < len(result)/2):
            if result[i] != result[-(i+1)]:
                return False                
            i+=1
        return True
        