/*
This function checks if num is even.
@param {number} num - The number to check.
@returns {boolean} - True if num is even, false otherwise.
*/
function isEven(num) {
  return num % 2 === 0;
}

/*
This function prints whether num is even or odd.
@param {number} num - The number to check.
@returns {void} - Prints the result to the console.
*/
function printNumberType(num) {
  if (isEven(num)) {
    console.log('The number is even.');
  } else {
    console.log('The number is odd.');
  }
}

printNumberType(3);
