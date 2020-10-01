"""
Detailed Version: Sep-30 2020
Joseph Yu
"""

class Solution(object):
    def validMountainArray(self, A):
        
        # if total length < 3: it can NOT be a mountain if there are only 1 or 2 items
        # if A is strictly upward hill: from small to large with NO peak
        # if A is strictly downward hill: from large to small with NO peak
        
        if len(A) < 3 or A == sorted(set(A)) or A[::-1] == sorted(set(A)):
            return False

        # 🎯 Locate the peak value position
        
        P = A.index(max(A)) + 1

        # 🎯 Test whether uphill and downhill are stictly Mountain Array
        # NOTE: Array[::-1] makes all items in reverse order
        # return (stircly uphill) and (strictly downhill)
        
        return A[:P] == sorted(set(A[:P])) and A[P-1:][::-1] == sorted(set(A[P-1:]))
    
"""
A = [0, 1, 3, 3, 3, 2, 2]

# Find out the peak value
print(max(A))

# Locate the first occurence of peak value
# NOTE: this the 1st occurence - it will ignore whatever afterwards 
print(A.index(max(A)))

# Convert back to Count No.
print(A.index(max(A))+1)

print(A[:3])

print(A[3-1:][::-1])

print(list(set(A[3-1:])))

3
2
3
[0, 1, 3]
[2, 2, 3, 3, 3]
[2, 3]
"""

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

"""
Detailed Version: Sep-30 2020
Joseph Yu
"""

class Solution(object):
    def validMountainArray(self, A):

        # Set total length of array as N
        N = len(A)

        # We use A[i] == Max as the relative position to represent peak
        # We should increment i along the walk up

        i = 0  # starting position

        # walk up the mountain
        # subtract "relative position" to represent position of i vs. i+1 as walk up

        while i+1 < N and A[i] < A[i+1]:
            i += 1  # increment i by 1 until the peak position

        # peak can NOT be the very first or very last
        # NOTE: position of i == 4 is the No.5th element
        # We need to compensate i by 1 >> i + 1

        # if i == 0 or i+1 == N means i is the very 1st and last item
        # Which should return False

        if i == 0 or i + 1 == N:
            return False

        # if neither the 1st or last, then we should consider to walk down
        # 🎯GOAL: check if all down-hill items are "strictly down"
        # NOTE this still works in parallel with ALL above statement

        while i+1 < N and A[i] > A[i+1]:
            i += 1

        # 😎 This final return implies we've finished and exhausted the downhill list
        # 🎯Goal: to return i == N-1 as True
        # and it should be the second to the last item >> True
        # E.g. {i = 7} == {N-1 = 8 - 1 = 7}
        # [0, 1, 2, 3, 4, 5, 6, 7]

        return i == N-1
