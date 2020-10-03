class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Set the array with ONLY unique values
        # Sort the set to return a sorted list: sort(set(list))
        # 👀 MUST add [:] to adjust in-place
        nums[:] = sorted(set(nums))
        return len(nums)

"""
📝 https://stackoverflow.com/questions/17457793/

sorting-a-set-of-values

>>> s = set(['0.000000000', '0.009518000', '10.277200999', '0.030810999', '0.018384000', '4.918560000'])
>>> sorted(s)
['0.000000000', '0.009518000', '0.018384000', '0.030810999', '10.277200999', '4.918560000']

>>> sorted(s, key=float)
['0.000000000', '0.009518000', '0.018384000', '0.030810999', '4.918560000', '10.277200999']

Note that sorted is giving you a list, not a set. That's because the whole point of a set, 
both in mathematics and in almost every programming language,* is that it's not ordered: 
the sets {1, 2} and {2, 1} are the same set.
"""

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
