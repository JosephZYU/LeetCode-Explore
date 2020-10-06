class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = [0] + nums
        
        for i in range(len(nums)):
            index = abs(nums[i])
            nums[index] = -abs(nums[index])
        
        return [i for i in range(len(nums)) if nums[i] > 0]
        
"""
https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3270/discuss/92955/Python-4-lines-with-short-explanation
"""
