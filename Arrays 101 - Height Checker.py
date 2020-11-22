class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))

"""        
# https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3228/discuss/299194/Python-1-liner
"""
