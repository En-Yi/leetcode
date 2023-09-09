class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ''
        temp = 0
        if len(a) < len(b):
            a = '0'*(len(b)-len(a)) + a
        if len(b) < len(a):
            b = '0'*(len(a)-len(b)) + b
        for i in range(len(a)):
            if int(a[-(i+1)]) + int(b[-(i+1)]) + temp == 3:
                result = '1' + result
                temp = 1
            elif int(a[-(i+1)]) + int(b[-(i+1)]) + temp == 2:
                result = '0' + result
                temp = 1
            elif int(a[-(i+1)]) + int(b[-(i+1)]) + temp == 1:
                result = '1' + result
                temp = 0
            elif int(a[-(i+1)]) + int(b[-(i+1)]) + temp == 0:
                result = '0' + result
                temp = 0
        if temp:
            result = '1' + result
        return result