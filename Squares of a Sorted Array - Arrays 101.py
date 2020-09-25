# Sample input
nums = [-4,-1,0,3,10]

# make every item to 2nd power and sort the array
def sortedSquares(A):
    return sorted(i**2 for i in A)

"""
Output: [0,1,9,16,100]

Ref - https://leetcode.com/problems/squares-of-a-sorted-array/discuss/310865/Python%3A-A-comparison-of-lots-of-approaches!-Sorting-two-pointers-deque-iterator-generator
"""
