class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1 # set up pointers for binary search

        while left <= right: # while search range is valid
            mid = (left + right)//2 # get the middle index

            if nums[mid] == target: # if the middle element is the target, return the index
                return mid
            elif nums[mid] > target: # otherwise if larger, reduce to left half
                right = mid-1
            else: # otherwise if smaller, reduce to right half
                left = mid+1
        
        return left