class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        result = ''.join(char.lower() for char in s if char.isalnum()) # joins each character onto an empty string, checking if the lowercase of each character in the string is an alphanumeric first

        return result == result[::-1] # compare the formatted string with its reverse