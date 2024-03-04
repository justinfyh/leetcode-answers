class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range (m, m+n): # for each index in the first array starting from n
            nums1[i] = nums2[i-m] # set it in place to the corresponding value in the second array

        nums1.sort() # sort the array in acsending order

        
        