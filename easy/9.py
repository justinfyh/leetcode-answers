class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1] # convert to string and compare with reversed