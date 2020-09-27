def merge(self, nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    nums1[:] = sorted(nums1[:m] + nums2[:n])
    
"""
Time complexity : \mathcal{O}((n + m)\log(n + m))O((n+m)log(n+m)).
Space complexity : \mathcal{O}(1)O(1).
"""
