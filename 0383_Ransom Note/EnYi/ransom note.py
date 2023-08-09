class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 先收集 magazine 的字母
        magazine_dict = {}
        for i in magazine:
            if i not in magazine_dict.keys():
                magazine_dict[i] = 1
            else:
                magazine_dict[i] += 1
        # 如果出現沒有在magazine內的字母或數量不對等則回傳錯誤
        for i in ransomNote:
            if i not in magazine_dict.keys() or magazine_dict[i] == 0:
                return False
            else:
                magazine_dict[i] -= 1
        return True