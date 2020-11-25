class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        # Initialize mx to represent the max on the right
        mx = -1
        
        # For loop reverse the order (start_inclusive, stop_non-inclusive, step)
        for i in range(len(arr)-1, -1, -1):
            
            # 🎯 Always compare current A[i] 🆚 maximum so far
            # 👍 Replace whatever is the maximum with mx
            # ⚡ Left_Next = Right_Current

            arr[i], mx = mx, max(mx, arr[i])
        
        # Return array after in-place change
        return arr

"""
print(list(range(len(A) -1, -1, -1)))

# range(start, stop, step)
# Start - Inclusive
# Stop - Not inclusive
"""
