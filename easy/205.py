class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        iso_dict = {} # initialise dictionareis
        rev_dict = {}

        for i in range(0, len(s)): # for every index in the string
            if s[i] not in iso_dict: # check if the character is not in the dictionary
                iso_dict[s[i]] = t[i] # add to dictionary
            elif iso_dict[s[i]] != t[i]: # otherwise check if its key value is the same as the char value in t at the same index
                return False # if it is not, return false

            if t[i] not in rev_dict: # do the same for t -> s dictionary
                rev_dict[t[i]] = s[i]
            elif rev_dict[t[i]] != s[i]:
                return False

        return True
        