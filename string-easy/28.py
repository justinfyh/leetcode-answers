class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        for i in range(0, len(haystack)): # iterate every character of haystack
            # if i+len(needle) > len(haystack):
            #     return -1

            substring = haystack[i:i+len(needle)] # get the substring at i, same length as needle

            if substring == needle: # if they are equal, return the index of the substring
                return i

        return -1 # otherwise return -1 if no occurence is found