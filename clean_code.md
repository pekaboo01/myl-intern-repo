Clean Code Principles

1. _Simplicity_ means writing code that is straightforward and avoids unnecessary complexity. The simpler the code, the easier it is to understand, test, and debug. Complex solutions may seem impressive, but they often create confusion and increase the risk of errors.

Simple code focuses on solving the problem directly without adding extra features or logic that are not needed. It follows the idea of doing one thing well instead of trying to handle everything at once.

2. _Readability_ means that the code should be easy for other developers to understand. This includes using clear variable names, proper formatting, consistent indentation, and meaningful comments when necessary.

Code is read more often than it is written. If someone cannot quickly understand what the code is doing, it becomes harder to maintain and improve. Good readability reduces misunderstandings and mistakes.

3. _Maintainability_ means that the code should be easy to modify or extend in the future. Software projects evolve over time, and changes are inevitable. If the code is messy or tightly coupled, making updates becomes difficult and risky.

Maintainable code is modular, well-structured, and organized into small reusable functions. This makes it easier for future developers — including yourself — to improve the code without breaking existing functionality.

4. _Consistency_ means following the same coding style, naming conventions, and structure throughout the project. This includes consistent formatting, file organization, and function naming.

When code is consistent, it feels predictable and easier to navigate. Teams often follow style guides to ensure everyone writes code in a similar way. This improves collaboration and reduces confusion.

5. _Efficiency_ means writing code that performs well and uses resources wisely. However, it is important to avoid premature optimization. Code should first be correct and readable before being optimized.

Efficient code improves performance, but it should not sacrifice clarity. A balance between performance and simplicity is important in real-world development.

**Messy code example:**

function x(a,b){if(a>0){if(b>0){return a\*b}else{return 0}}else{return 0}}

This makes it difficult for another developer to quickly understand the purpose of the function. Because of the following reasons:

-The function name x does not explain what it does.
-The parameters a and b are unclear.
-Everything is written in one line.
-Nested conditions make it harder to follow.
-There are no comments or formatting.

A much cleaner way:

function multiplyIfPositive(numberOne, numberTwo) {
if (numberOne <= 0 || numberTwo <= 0) {
return 0;
}

return numberOne \* numberTwo;
}

This is cleaner simply because:

-The function name clearly describes its purpose.
-Variable names are meaningful.
-Proper formatting improves readability.
-The condition is simplified.
-The logic is easier to follow.

And so, clean code principles are important because they improve collaboration, reduce bugs, and make future updates easier. Writing simple, readable, maintainable, consistent, and efficient code ensures that projects remain stable and scalable over time.

=====================================================================================================================

1. Why is code formatting important?

Code formatting is important because it makes your code consistent, readable, and maintainable. When everyone follows the same style, it’s easier to understand what the code does, spot mistakes, and collaborate with teammates. Poorly formatted code can cause confusion, lead to errors, and make debugging harder.

2. What issues did the linter detect?

no-unused-vars - Variables like unused or test were declared but never used.
no-undef - A typo like consol instead of console.

These are the kind of issues that don’t necessarily stop the code from running but can lead to bugs or make the code harder to understand.

3. Did formatting the code make it easier to read?

Yes, running Prettier and ESLint made the code easier to read. Indentation, spacing, and semicolons were corrected, which improves clarity. Clean formatting helps you and your teammates quickly see the structure of the code, understand the logic, and reduces mistakes when making changes.

=======================================================================================================================

1. Research Best Practices for Naming Variables and Functions

Here are widely accepted practices:

_Variables_

Be descriptive: Names should convey the purpose of the variable.

Good - userAge (clearly stores a user's age)
Bad - x (unclear what it stores)

Use camelCase (JavaScript, Java, etc.) or snake_case (Python, Ruby)
Avoid abbreviations unless widely known:

Bad - usrAg
Good - userAge

Boolean variables should sound like yes/no questions:

Good - isActive, hasPermission
Bad - status (too vague)

_Functions_

Use verbs or verb phrases to indicate action:

Good - calculateTotal(), sendEmail()
Bad - total(), email()

2. Example of Unclear Variable Names

function m(d, a) {
let t = 0;
for (let i = 0; i < a.length; i++) {
t += a[i];
}
return t / d;
}

let r = m(5, [10, 20, 30, 40, 50]);
console.log(r);

Issues:

-Function m (no idea what it does)
-Parameters d and a (unclear)
-Variable t (unclear)
-Variable r (unclear)

3. Refactored Version for Clarity

function calculateAverage(numberOfValues, values) {
let totalSum = 0;
for (let i = 0; i < values.length; i++) {
totalSum += values[i];
}
return totalSum / numberOfValues;
}

let averageScore = calculateAverage(5, [10, 20, 30, 40, 50]);
console.log(averageScore);

Improvements:

-calculateAverage (clearly describes the function)
-numberOfValues and values (descriptive parameters)
-totalSum (clearly describes what the variable stores)
-averageScore (meaningful variable name)

_Reflection_

1. What makes a good variable or function name?

A good variable or function name is one that clearly tells you what it is or what it does without needing extra explanation. For variables, the name should describe the data it holds. For example, `userAge` is better than just `x` because anyone reading the code can quickly understand that this variable stores the age of a user. For functions, the name should usually start with a verb to show the action it performs, like `calculateTotal()` or `sendEmail()`. Names should also be consistent, easy to read, and avoid unnecessary abbreviations. If someone new looks at your code, good names should make it almost self-explanatory.

2. What issues can arise from poorly named variables?

Poorly named variables and functions can make code very hard to read and understand. If a variable has a vague name like `t` or a function is called `m`, it is not clear what the code is doing. This can cause mistakes when someone tries to use or modify the code because they might misunderstand its purpose. Poor names can also make collaboration harder since other programmers will spend extra time figuring out what everything means. Over time, this can make the code messy and harder to maintain.

3. How did refactoring improve code readability?

Refactoring the code by giving variables and functions better names made it much easier to understand. For example, changing the function name from `m` to `calculateAverage` immediately tells you what the function does. Changing variable names like `t` to `totalSum` or `r` to `averageScore` makes it clear what each value represents. Overall, reading the code now feels smoother and more logical. You can almost understand the logic just by reading the names, without needing to follow each line carefully. This not only saves time but also reduces the chance of errors and makes it easier for others to work with the code.

=======================================================================================================================

1. Research Best Practices for Small, Focused Functions

-Single Responsibility – Each function should do one thing.
calculateAverage() → calculates average (Good)
calculateAverageAndPrintReport() → doing two things at once (Wrong)
-Short and readable – A function should be short enough to fit in one screen if possible.
-Descriptive names – The function name should tell exactly what it does.
-Avoid side effects – Functions should ideally return values instead of directly modifying global data.
-Reuse and modularity – Small functions can be reused in multiple places.

2. Example of a Long, Complex Function

function processNumbers(numbers) {
let sum = 0;
let max = numbers[0];
let min = numbers[0];

    for (let i = 0; i < numbers.length; i++) {
        console.log("Number:", numbers[i]);
        sum += numbers[i];
        if (numbers[i] > max) max = numbers[i];
        if (numbers[i] < min) min = numbers[i];
    }

    let average = sum / numbers.length;
    console.log("Sum:", sum);
    console.log("Average:", average);
    console.log("Max:", max);
    console.log("Min:", min);

}

processNumbers([10, 20, 30, 5, 15]);

Issues:

-One function does everything → printing, calculating sum, max, min, average
-Hard to reuse parts, like if you only wanted the average
-Harder to debug

3. Refactored Version with Small, Focused Functions

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

Improvements:

-Each function has one clear job
-Logic is reusable (e.g., calculateAverage can be used anywhere)
-Easier to read, test, and maintain

_Reflection_

1. Why is breaking down functions beneficial?

Breaking down large functions into smaller ones is very helpful because it makes code easier to read, understand, and maintain. When each function has a single job, it is clear what it does and how it fits into the bigger picture. Small functions are also easier to test, debug, and reuse in different parts of the program. Without small functions, large blocks of code can become confusing, hard to modify, and prone to errors.

2. How did refactoring improve the structure of the code?

Refactoring the original function into smaller ones improved the code a lot. Now, each part of the logic—like calculating averages, finding the highest or lowest grade, or printing student information—is in its own function. This separation of responsibilities makes the code cleaner and easier to follow. If we need to change how we calculate the average, we only need to update the `calculateAverage` function without touching anything else. The structure is now organized, logical, and much easier for others (or even ourselves in the future) to understand.

======================================================================================================================

1. Research the DRY Principle

-DRY = Don’t Repeat Yourself
-The idea is that every piece of knowledge or logic should exist in only one place in your code.

Benefits of DRY:

-Easier to maintain (you only need to update in one place)
-Less chance of mistakes (no conflicting versions)
-Cleaner, more readable code

2. Example of Duplicated Code

function printUserInfo(user1, user2) {

    console.log("Name:", user1.name);
    console.log("Age:", user1.age);
    console.log("Email:", user1.email);

    console.log("Name:", user2.name);
    console.log("Age:", user2.age);
    console.log("Email:", user2.email);

}

const user1 = { name: "Alice", age: 25, email: "alice@example.com" };
const user2 = { name: "Bob", age: 30, email: "bob@example.com" };

printUserInfo(user1, user2);

Issues:

-The printing logic for user1 and user2 is duplicated
-If you want to change how user info is printed, you have to update both places
-Hard to reuse for more than two users

3. Refactored Version to Avoid Duplication

function printSingleUser(user) {

    console.log("Name:", user.name);
    console.log("Age:", user.age);
    console.log("Email:", user.email);

}

function printAllUsers(users) {

    for (let i = 0; i < users.length; i++) {
        printSingleUser(users[i]);
        console.log("-----"); // separator
    }

}

const users = [
{ name: "Alice", age: 25, email: "alice@example.com" },
{ name: "Bob", age: 30, email: "bob@example.com" }
];

printAllUsers(users);

Improvements:

-printSingleUser handles printing one user (no repetition)
-printAllUsers loops through any number of users (scalable)
-Changing the format now only requires updating printSingleUser

_Reflection_

1. What were the issues with duplicated code?

Duplicated code makes programs harder to maintain and more error-prone. When the same logic appears in multiple places, you have to update every copy if something changes. This can easily lead to mistakes or inconsistencies. Duplication also makes the code longer, harder to read, and less reusable. For example, in our first version, printing user information was repeated for each user. If we wanted to add a new detail, we would have had to change it in multiple places, which is inefficient and risky.

2. How did refactoring improve maintainability?

Refactoring the code into a single function for printing a user eliminated repetition. Now, the logic exists in only one place. The main function that handles multiple users just calls this small function in a loop. This approach makes the code easier to read, update, and reuse. If we want to change the format of how user information is printed, we only need to change `printSingleUser`, and it automatically applies to all users. The code is cleaner, shorter, and much more maintainable.
