class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Set up inital count as the starting base
        count = 0
        max_count = 0
        # For loop
        for num in nums:
            # Increment count if num equals 1
            if num == 1:
                count += 1
            # Store max_count and set count back to 0
            elif num == 0:
                # Compare the most current count with the up-to-date max_count and save the historical maximum number
                max_count = max(max_count, count)
                # Set count back to 0
                count = 0
        # Final rap up incase if the last one is the maximum count of all time
        return max(max_count, count)
