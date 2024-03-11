package easy;

class Solution {
    public boolean isPalindrome(int x) {
        String y = Integer.toString(x); // convert to string
        
        StringBuilder input1 = new StringBuilder(); // create a string builder
 
        input1.append(y); // add input to string builder
 
        String z = input1.reverse().toString(); // reverse input

        if (y.equals(z)) { // check if input and reversed are equal, if so, return true
            return true;
        }
        else { //  otherwise return false
            return false;
        }
    }
}