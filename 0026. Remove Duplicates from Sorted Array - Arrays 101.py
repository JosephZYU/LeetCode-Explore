class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Set the array with ONLY unique values
        # Sort the array
        # 👀 MUST add [:] to adjust in-place
        nums[:] = sorted(set(nums))
        return len(nums)

"""
Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.


Runtime: 72 ms, faster than 99.50% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 16 MB, less than 5.28% of Python3 online submissions for Remove Duplicates from Sorted Array.

https://leetcode.com/problems/remove-duplicates-from-sorted-array/discuss/507271/Simple-Python-beats-100
"""
