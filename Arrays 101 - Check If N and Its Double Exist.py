class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # Count if there are more than 1 zero
        if arr.count(0) > 1: 
            return True
        
        # Remove potential zeroes from the set
        S = set(arr) - {0}
        
        # Check if N and Its Double Exist
        for i in arr:
            if 2*i in S:
                return True
        
        # If non of the above met, return False
        return False
        
"""
Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.
Example 2:

Input: arr = [7,1,14,11]
Output: true
Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.
Example 3:

Input: arr = [3,1,7,11]
Output: false
Explanation: In this case does not exist N and M, such that N = 2 * M.

https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/discuss/503507/Python-3-(five-lines)-(beats-100)
"""
