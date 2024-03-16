class Solution:
    def reverseWords(self, s: str) -> str:
        string = "" # initialise result
        s = s.split() # split the input string by any whitespaces

        for i in s[::-1]: # for every word in the string, add it to the result in reverse order
            string += " " + i

        return string.strip() # strip the string of leading and trailing whitespaces and return