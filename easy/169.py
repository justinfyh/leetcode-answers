class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort() # sort in order
        return (nums[floor(len(nums)/2)]) # return the middle element which will always be majority if it is always more than n/2