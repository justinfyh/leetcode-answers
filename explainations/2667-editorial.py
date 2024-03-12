function log(inputFunction) { # Higher order function, taking a fuction as input
    return function(...args) { # Enhances and returns a new function 
        console.log("Input", args); # Logs arguements of the input function
        const result = inputFunction(...args); # Runs the function to get the result
        console.log("Output", result); # Logs the result of the function
        return result; # Returns the result
    }
}
const f = log((a, b) => a + b); # Inside () is the function being inputted
f(1, 2); // Logs: Input [1, 2] Output 3 # Basically just adds log statements to the original function