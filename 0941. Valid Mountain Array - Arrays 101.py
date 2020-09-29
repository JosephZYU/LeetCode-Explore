class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A)<3 or A == sorted(set(A)) or A[::-1] == sorted(set(A)):
            return False

        l = A.index(max(A))+1

        return A[:l] == sorted(set(A[:l])) and A[l-1:][::-1] == sorted(set(A[l-1:]))

"""
Example 1:

Input: [2,1]
Output: false
Example 2:

Input: [3,5,5]
Output: false
Example 3:

Input: [0,3,2,1]
Output: true

https://leetcode.com/problems/valid-mountain-array/discuss/201958/python-easy
"""
