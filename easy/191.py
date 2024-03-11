class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0 # set counter
        
        for i in bin(n)[2:]: # for every element in n in binary 
            if i == '1': # check if it is a 1, if so increment counter
                count += 1

        return count