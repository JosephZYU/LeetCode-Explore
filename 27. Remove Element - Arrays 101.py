class Solution:
    def removeElement(self, nums, val):
    
        # Count how many occurrence of given val in the list
        # 👀 make sure to put range() to make it iterable
        for i in range(nums.count(val)):
            nums.remove(val)
            
        # Return the length after in-place removal
        return len(nums)

"""
Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Accepted
Runtime: 32 ms
Your input
[3,2,2,3]
3
Output
[2,2]
Expected
[2,2]

https://leetcode.com/problems/remove-element/discuss/12306/Simple-Python-O(n)-two-pointer-in-place-solution/12810

"""
