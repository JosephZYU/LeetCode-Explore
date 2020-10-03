class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        
        # initialize two pointers i = 0, j = 0 
        i = 0
        
        # Iterate j over range(len(nums)): [0, 1, 2, ...]
        for j in range(len(A)):
            
            # 🎯 Always relocate even number to the furtherest left position possible
            # Swap nums[i] and nums[j] given even number
            if A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]
                
                # 🎯 move point i to the most-left odd number so far
                # Increment i by 1
                i += 1
        
        return A
