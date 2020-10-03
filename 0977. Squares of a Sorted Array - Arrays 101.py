class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        
        # 🎯 Square of each item
        for i in range(len(A)):
            A[i] *= A[i]
            
        # 🎯 Using built in sort.
        A.sort()
        
        return A

"""
https://leetcode.com/problems/squares-of-a-sorted-array/discuss/310865/Python%3A-A-comparison-of-lots-of-approaches!-Sorting-two-pointers-deque-iterator-generator
"""
