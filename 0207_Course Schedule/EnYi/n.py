class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        ans = []

        for pair in prerequisites:
            course = pair[0]
            prerequisite = pair[1]
            adj[prerequisite].append(course) # prerequisite的位置存後修course
            indegree[course] += 1 # 紀錄course的先修數量

        queue = deque() # 雙向queue
        for i in range(n):
            if indegree[i] == 0: # 如果該course沒有先修
                queue.append(i) # 加入雙向queue

        while queue:
            current = queue.popleft() # 取出雙向queue第一個
            ans.append(current) # 放入 ans 收集沒有先修的course

            for next_course in adj[current]: # 尋找以current為先修的 course
                indegree[next_course] -= 1 # 該course的先修數量-1
                if indegree[next_course] == 0: # 如果該course的先修數量變為0
                    queue.append(next_course)
        # 如果ans能收集全部course則表示沒有cycle
        return len(ans) == n