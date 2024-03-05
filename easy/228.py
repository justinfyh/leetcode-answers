class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0: # check if it is an empty array
            return []

        l = nums[0] # initialise lower and higher indices
        h = nums[0]
        result = [] # initialise output array

        for i in range(0, len(nums)): # for each index in the array
            if i == len(nums) - 1: # check if it is the last index in the array 
                if l == h: # if l and h are the same, add appriopriate string
                    result.append(str(l))
                else: # otherwise concatenate and add string to arrau
                    result.append(str(l) + '->' + str(h))
                break # exit the loop

            if nums[i] + 1 != nums[i+1]: # check of the next element in the array is not equal to the current value + 1 
                if l == h: # if l and h are the same, add appriopriate string
                    result.append(str(l))
                else: # otherwise concatenate and add string to arrau
                    result.append(str(l) + '->' + str(h))
                l = nums[i+1] # set low and high to the next element in the array
                h = nums[i+1]
            else: # otherwise set high to the next element in the array
                h = nums[i+1]

        return result # return the array
