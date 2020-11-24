class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        # previous and current length of consecutive 1 
        pre, curr, maxlen = -1, 0, 0
        
        
        for n in nums:
            if n == 0:
                pre, curr = curr, 0
            else:
                curr += 1
            maxlen = max(maxlen, pre + 1 + curr )
        
        return maxlen


"""
https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3230/discuss/96946/Concise-Python-solution-good-for-follow-up-time-O(n)-space-O(1)
"""
