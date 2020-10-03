class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # initialize two pointers i = 0, j = 0 
        i = 0
        
        # Iterate j over range(len(nums)): [0, 1, 2, ...]
        for j in range(len(nums)):
            
            # 🎯 Always relocate non-zeroe digits to the furtherest left position possible
            # Swap nums[i] and nums[j] given non-zero
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                
                # 🎯 move point i to the most-left zero so far
                # Increment i by 1
                i += 1
                

"""
https://leetcode.com/problems/move-zeroes/discuss/208755/Python-solution
"""
