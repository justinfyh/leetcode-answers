class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        for n in range(0, len(nums)): # for every element in the array
            nums[n] *= nums[n] # square it in place

        nums.sort() # sort array in ascending order

        return nums # return array