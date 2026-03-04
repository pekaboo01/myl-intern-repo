function isEven(num) {
  return num % 2 === 0;
}

function printNumberType(num) {
  if (isEven(num)) {
    console.log('The number is even.');
  } else {
    console.log('The number is odd.');
  }
}

printNumberType(3);
