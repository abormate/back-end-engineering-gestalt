/*
Write a function factorial() that takes a number as an argument and returns the factorial of the number.

Example:

factorial(6); 
// returns `720` because 6 * 5 * 4 * 3 * 2 * 1 = 720 
*/

const factorial = num => {
  let result = 1;
  
  for (let i=num; i>0; i--) {
    result *= i;
  }

  return result;
}
