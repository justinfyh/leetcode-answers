class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0 # initialise double pointers
        j = 0

        while nums1[i] != nums2[j]: # while the values are not equal
            if nums1[i] < nums2[j]: # if element in nums2 is greater, increment nums1
                i += 1
            else: # otherwise increment nums2
                j += 1

            if i >= len(nums1) or j >= len(nums2): # check if either have gone out of bounds, if so, return -1 as no matching element
                return -1

        return nums1[i] # return the matching element