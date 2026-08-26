class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclidean = lambda x: x[0] ** 2 + x[1] ** 2
        
        def partition(l, r):
            pivot_idx = r
            pivot_dist = euclidean(points[pivot_idx])
            i = l
            for j in range(l, r):
                if euclidean(points[j]) <= pivot_dist:
                    points[i], points[j] = points[j], points[i]
                    i += 1
                  
            points[i], points[pivot_idx] = points[pivot_idx], points[i]        
            return i

        pivot = len(points)
        L = 0
        R = len(points) - 1

        while pivot != k:
            pivot = partition(L, R)
            if pivot < k:
                L = pivot + 1
            else:
                R = pivot - 1
            # print(pivot, L, R)    
        return points[:k]             
