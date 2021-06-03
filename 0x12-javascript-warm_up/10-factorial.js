#!/usr/bin/node
// prints the factorial of an argument
function factorial(n) {
    if (!n || n <= 0) {
        return 1;
    }
    return n * factorial (n - 1);
}
console.log(factorial(parseInt(process.argv[2])));
