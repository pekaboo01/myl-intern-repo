function calculateSum(numbers) {
  let sum = 0;

  if (!Array.isArray(numbers)) {
    console.log('Error: Input must be an array.');
    return null;
  }

  if (numbers.length === 0) {
    console.log('Error: Array cannot be empty.');
    return null;
  }

  for (let i = 0; i < numbers.length; i++) {
    if (typeof numbers[i] !== 'number') {
      console.log('Error: All elements must be numbers.');
      return null;
    }
    sum += numbers[i];
  }

  return sum;
}

function calculateAverage(numbers) {
  return calculateSum(numbers) / numbers.length;
}

let numbers = [1, 'a', 3, 4, 5];
console.log(calculateAverage(numbers));
