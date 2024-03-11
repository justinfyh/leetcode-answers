class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(len(digits)-1, -1, -1): # reverse the indexing for the array
            if digits[i] == 9: # if the element is 9, make it 0
                digits[i] = 0
            else: # otherwise add one to the element and return the array
                digits[i] += 1
                return digits

        return [1] + digits # if the lowest element is 9, we need to append a 1 