class Solution:
    def pivotInteger(self, n: int) -> int:
        array = [] # create a new array
        for i in range(1, n + 1): # add 1 to n inclusive to the array
            array.append(i)

        # for every element in the array x, check if 1 to x and x+1 to n are equal, if so return x
        for x in range(1, n+1):
            print(sum(array[0:x]))
            if sum(array[0:x]) == sum(array[x+1:len(array)]):
                return array[x]

        # if no pivot found
        return -1