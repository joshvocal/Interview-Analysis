# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


'''
Solution 1: Heap
Time: O(n*k + log k) // n elements in the list, k elements in list
Space: O(n)
'''

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        
        if not lists or len(lists) == 0:
            return None
        
        for list in lists:
            while list:
                heap.append(list.val)
                list = list.next
                
        heapq.heapify(heap)        
        
        if not heap:
            return None
        
        head = ListNode(heapq.heappop(heap))
        dummy = head
        while heap:
            head.next = ListNode(heapq.heappop(heap))
            head = head.next
            
        return dummy
            