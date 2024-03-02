class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0 # initialise length output

        for char in s[::-1]: # reverse string and for every character
            if char != " ": # if it is not an empty space, add 1 to the length
                length += 1
            elif char == " " and length != 0: # otherwise if it is an empty space and length is not 0 (accounting for strings ending with space instances) return the length
                return length
        
        return length