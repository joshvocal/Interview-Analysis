import heapq

class Solution:
    def kthSmallest(self, matrix: 'List[List[int]]', k: 'int') -> 'int':
        q = []
        n = len(matrix) 

        for i in range(0, n):
            for j in range(0, n):
                heapq.heappush(q, matrix[i][j])
                if len(q) > n * n - k + 1:
                    heapq.heappop(q)
                
        return heapq.heappop(q)
                    