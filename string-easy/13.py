class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = { # create a dictionary of the roman numerals and their values
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        result = 0 # initialise result variable
        prev_value = 0 # initialise variable for the previous loop value

        for char in s[::-1]: # reverse the string and for every character
            if dictionary[char] < prev_value: # check if it is less than the previous character
                result -= dictionary[char] # if so, subtract from result
            else:
                result += dictionary[char] # otherwise add to result

            prev_value = dictionary[char] # set the new previous value 

        return result # return the result
