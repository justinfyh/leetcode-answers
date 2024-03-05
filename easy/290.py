class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_dict = {} # initialise dictionary

        s = s.split(' ') # split string into a list

        if len(s) != len(pattern): # check if the length of string and list are equal
            return False
        
        for i in range(0, len(pattern)): # for each index
            if pattern[i] not in word_dict and s[i] not in word_dict.values(): # check if the character key and value are not in the dictionary
                word_dict[pattern[i]] = s[i] # add to dictionary
            elif  pattern[i] not in word_dict and s[i] in word_dict.values(): # otherwise check if the value is in but not the char key
                return False
            elif word_dict[pattern[i]] != s[i]: # otherise check if the key value and list value match
                return False

        return True