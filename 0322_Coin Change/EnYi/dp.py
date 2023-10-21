class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp 解法，從小到大找組合
        dp = [amount+1]*(amount+1) # 起始較大的值為了比較和更新，長度為amount+1
        dp[0] = 0 # 金額0則0個硬幣
        coins.sort() # 小到大排序
        
        for a in range(1, amount+1): # 找尋每個金額組合
            for c in coins: # 找尋每種幣值
                if a - c >= 0: # 如果可用 c 幣值
                    dp[a] = min(dp[a], 1+ dp[a-c]) # 第二項表示用c幣值 一枚，加剩餘的組合
                else:
                    break
        # 最後返回 如果指定金額有更新表示可以由coins組合，且必定找到最小數量，否則返回無解
        return  dp[amount] if dp[amount] != amount+1 else -1