function printNumbers(numbers) {
  for (let i = 0; i < numbers.length; i++) {
    console.log(numbers[i]);
  }
}

function calculateSum(numbers) {
  let sum = 0;
  for (let i = 0; i < numbers.length; i++) {
    sum += numbers[i];
  }
  return sum;
}

function findMax(numbers) {
  let max = numbers[0];
  for (let i = 1; i < numbers.length; i++) {
    if (numbers[i] > max) {
      max = numbers[i];
    }
  }
  return max;
}

function findMin(numbers) {
  let min = numbers[0];
  for (let i = 1; i < numbers.length; i++) {
    if (numbers[i] < min) {
      min = numbers[i];
    }
  }
  return min;
}

function printSummary(numbers) {
  let sum = calculateSum(numbers);
  let max = findMax(numbers);
  let min = findMin(numbers);
  let average = sum / numbers.length;

  console.log(`Sum: ${sum}`);
  console.log(`Max: ${max}`);
  console.log(`Min: ${min}`);
  console.log(`Average: ${average}`);
}

let numbers = [10, 20, 30, 5, 15];

printNumbers(numbers);
printSummary(numbers);
