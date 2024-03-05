class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = {} # initialise a dictionary

        for char in magazine: # for every character in magazine
            magazine_dict[char] = magazine_dict.get(char, 0) + 1 # update its frequency in the dictionary
        
        for char in ransomNote: # for every character in ransomNote
            if magazine_dict.get(char) == 0 or char not in magazine_dict: # if its value in dictionary is 0 or if it doesnt exist in the dictionary
                return False
            else: # otherwise decrement the chars frequency in the dictionary by 1
                magazine_dict[char] = magazine_dict.get(char) - 1
        
        return True