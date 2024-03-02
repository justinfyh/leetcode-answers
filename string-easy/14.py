class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(0, len(strs[0])): # for every letter in the first string
            temp = strs[0][i] # assign letter to temp variable

            for j in range(0, len(strs)): # then for every string in the array
                if (len(strs[j]) == i or strs[j][i] != temp): # check if the corresponding character is not equal to the temp, or if the string is the same length as the first string. Must test for length first otherwise out of index
                    return strs[j][:i] # if so, return the current string -1 character

        return strs[0] # otherwise return the first string