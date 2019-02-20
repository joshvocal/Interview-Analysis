import heapq


"""
Solution 1: Heap
Time: O(n*log n)
Space: O(n)
"""

class Solution:
    def findKthLargest(self, nums, k):
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(nums) > k:
                heapq.heappop(heap)

        return heapq.heappop(heap)


"""
Solution 2: Reverse
Time: O(log n)
Space: O(n)
"""

class Solution2:
    def findKthLargest(self, nums, k):
        nums.sort(reverse=True)
        return nums[k - 1]


"""
Solution 3: Heap
Time: O(n*log n)
Space: O(n)
"""

class Solution:
    def findKthLargest(self, nums, k):
        heapq.heapify(nums)

        while len(nums) >= k:
            heapq.heappop(nums)

        return heapq.heappop(nums)




