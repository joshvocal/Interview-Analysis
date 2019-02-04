class Solution:

    """
    Solution 1: HashMap
    Time: O(n)
    Space: O(n)
    """

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hash_map = {}
        intersec = []

        for num in nums1:
            hash_map[num] = hash_map.get(num, 0) + 1

        for num in nums2:
            if num in hash_map and hash_map[num] > 0:
                intersec.append(num)
                hash_map[num] = hash_map[num] - 1

        return intersec
    