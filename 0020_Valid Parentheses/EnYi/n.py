class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(":")",
                "[":"]",
                "{":"}"}
        p = ['0']
        
        for i in s:
            if i in pairs.keys():
                # 只要是左括弧，全都加入
                p.append(i)
            
            elif i in pairs.values():
                # 右括弧的話，list若沒有其他元素則回傳錯誤
                if len(p) == 1:
                    return False
                # 或是比對list最後一項是否為對應的key
                elif p[-1] == list(pairs.keys())[list(pairs.values()).index(i)]:
                    # 是則取出
                    p.pop()
                else:
                    return False
        
        if len(p) == 1:
            return True
        else:
            return False