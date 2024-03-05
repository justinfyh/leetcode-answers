class Solution:
    def isValid(self, s: str) -> bool:
        paren_dict = { # define opening parenthesis as keys with closing parenthesis as their values
            '(': ')',
            '{': '}',
            '[': ']',
        }
        stack = [] # initialise a stack

        if len(s) % 2 == 1: # if the length of the string is odd, then return false as it is not balanced
            return False

        for char in s: # for every character in the string
            if char == '(' or char == '{' or char == '[': # if it is an opening parenthesis
                stack.append(paren_dict[char]) # add its corresponding closing parenthesis to the stack
            else: # otherwise if it is a closing parenthesis
                if len(stack) == 0: # if the stack is empty, there is no corresponding opening parenthesis, so false
                    return False
                if stack.pop() != char: # pop the last value in the stack and comapre it to the current char, if not equal then false
                    return False

        if len(stack) != 0: # if the stack has not been cleared, return false
            return False

        return True
