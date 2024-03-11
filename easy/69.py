class Solution:
    def mySqrt(self, x: int) -> int: # BINARY SEARCG
        left, right = 1, x # set left and right pointers
        
        while left <= right: # while the search area is valid
            mid = (left + right)//2 # find the middle

            if mid*mid == x: # if the middle is the square root, return it
                return mid
            elif mid*mid > x: #if the middle is greater than the square root
                right = mid-1 # reduce the array to the left half
            else: # if the middle is less than the square root
                left = mid+1 # reduce the array to the right half
                
        return right # otherwise return the right index
