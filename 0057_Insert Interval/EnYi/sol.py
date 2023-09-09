class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left = newInterval[0]
        right = newInterval[1]
        intervals.insert(0,[-2,-1])
        intervals.insert(len(intervals),[1e5+1, 1e5+2])
        impact = []
        indirect = []
        for i in range(len(intervals)-1):
            if intervals[i][0] <= left and left <= intervals[i][1]:
                impact.append(i)
            if intervals[i][1] < left and left < intervals[i+1][0]:
                indirect.append(i+1) # 影響第i+1個interval之後
            if intervals[i][1] < right and right < intervals[i+1][0]:
                indirect.append(i) # 影響第i個interval之後，i+1之前
            if intervals[i][0] <= right and right <= intervals[i][1]:
                impact.append(i)
        if len(impact) == 2:   
            if impact[0] == impact[1]:
                return intervals[1:len(intervals)-1]
            if impact[0] < impact[1]:
                left = min(left, intervals[impact[0]][0])
                right = max(right, intervals[impact[1]][1])
                del intervals[impact[0]:impact[1]+1]
                intervals.insert(impact[0], [left, right])
                return intervals[1:len(intervals)-1]
        if len(indirect) == 2:
            if indirect[0] == indirect[1]: # 包到一個
                intervals[indirect[0]] = [left, right]
                return intervals[1:len(intervals)-1]
            if indirect[0] > indirect[1]: # 沒包到
                intervals.insert(indirect[0], [left, right])
                return intervals[1:len(intervals)-1]
            if indirect[0] < indirect[1]: # 包到兩個以上
                # 刪除包到的，插入新的
                del intervals[indirect[0]:(indirect[1]+1)]
                intervals.insert(indirect[0], [left, right])
                return intervals[1:len(intervals)-1]
# 還有各一邊的*2
        if len(impact) == 1 and len(indirect) == 1:
            if impact[0] == indirect[0]:
                intervals[impact[0]][0] = min(left, intervals[impact[0]][0])
                intervals[impact[0]][1] = max(right, intervals[impact[0]][1])
                return intervals[1:len(intervals)-1]
            if impact[0] != indirect[0]:
                intervals[min(impact[0], indirect[0])][0] = min(intervals[min(impact[0], indirect[0])][0], left)
                intervals[min(impact[0], indirect[0])][1] = max(right, intervals[impact[0]][1])
                del intervals[(min(impact[0], indirect[0])+1):(max(impact[0], indirect[0])+1)]
                return intervals[1:len(intervals)-1]