class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclidean_distance(x, y):
            return ((x[0]-y[0])**2 + (x[1]-y[1])**2)**(1/2)
        dist_list = [euclidean_distance([0,0],i) for i in points]
        # sorted index
        s = sorted(range(len(dist_list)), key=lambda k: dist_list[k])
        return [points[i] for i in s[0:k]]
    