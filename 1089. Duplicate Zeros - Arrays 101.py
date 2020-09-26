def duplicateZeros(arr):

    # count how many 0 from the original array
    zeroes = arr.count(0)
    # measure the length of the original array
    n = len(arr)

    # work backwards
    # [7, 6, 5, 4, 3, 2, 1, 0]

    for i in range(n-1, -1, -1):
        if i + zeroes < n:
            arr[i + zeroes] = arr[i]
        if arr[i] == 0: 
            zeroes -= 1
            if i + zeroes < n:
                arr[i + zeroes] = 0

"""
Input: [1, 0, 2, 3, 0, 4, 5, 0]

Output:[1, 0, 0, 2, 3, 0, 0, 4]
"""

"""
Why backwards?
If we would start shifting from left to right, then we would be overwriting elements before we have had the chance to shift them,
that is why we go backwards instead.
We make sure we have shifted out an element before we shift another one into its original position.

What is the correct shift distance?
The duplication of a zero pushes all elements to the right of it by one.
This means also that every element is shifted to the right as many times as there are zeroes to the left of it.
E.g. in the array [1,0,2,0,3] , 1 will not move, 2 will shift one position and 3 will shift two positions.
As we go backwards, every time we bypass a zero (and duplicate it), the shift distance decreases for the elements we haven't shifted yet, because there is one less zero in front of them.

Why the < n checks?
Shifts push some of the elements out of the array. We do the < n checks to make sure we write down only elements that are shifted to a valid position inside the array and we ignore the ones falling off the end.

https://leetcode.com/problems/duplicate-zeros/discuss/322576/Python-3-real-in-place-solution

"""
