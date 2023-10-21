class TrieNode:
    def __init__(self):
        self.children = {} # 字典，儲存該節點的子節點，key是字元，value是對應的trienode 物件
        self.is_end_of_word = False # 路徑是否構成完整的單字
class Trie:
    
    def __init__(self):
        self.root = TrieNode() # 根節點沒有字元，為trie結構的起點

    def insert(self, word: str) -> None:
        node = self.root
        for char in word: # 依序找尋trie的每個字元
            if char not in node.children: # 如果沒有出現在子節點中
                node.children[char] = TrieNode() # 新增節點
            node = node.children[char]
        node.is_end_of_word = True # 找完最後一個字尾設為終點

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children: # 如果沒出現在子節點則返回false
                return False
            node = node.children[char] # 有則依該字元的子節點往下找
        return node.is_end_of_word # 如果為最後的節點則返回 true

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)