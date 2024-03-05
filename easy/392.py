class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0 # initialise index for both strings
        j = 0

        while j < len(t) and i < len(s): # while the indices do not exceed the string lengths
            if s[i] == t[j]: # if there is a matching value, increment both indices
                i += 1
                j += 1
            else: # otherwise increment t index only
                j += 1

        if i == len(s): # if the s index matches the length of s (all letters read) return true
            return True
        else: # otherwise return false
            return False