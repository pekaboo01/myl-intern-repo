1. Research common code smells and how they impact code quality.

Code smells are warning signs in code that indicate possible design problems. They do not always mean the code is broken, but they suggest that the code may become hard to maintain, understand, or extend in the future.

Code smells reduce readability and increase complexity. They make debugging harder, increase the risk of bugs, and make future changes more difficult. Over time, they can make a project fragile and difficult to maintain.

2. Code Smell Examples and Refactoring

_Magic Numbers and Strings_

Hardcoded values are used directly in the code without explanation.

Example:
function calculateDiscount(price) {
return price \* 0.8;
}

if (user.role === "VIP") {
console.log("Special access granted");
}

Problem:
-0.8 is unclear.
-"VIP" is repeated and hardcoded.

Refactored version:
const VIP_ROLE = "VIP";
const VIP_DISCOUNT_RATE = 0.2;

function calculateDiscount(price) {
return price \* (1 - VIP_DISCOUNT_RATE);
}

if (user.role === VIP_ROLE) {
console.log("Special access granted");
}

Now the values are clearly defined and easy to change.

_Long Function_

A function does too many things.

Example:
function processOrder(order) {
let total = 0;

    for (let i = 0; i < order.items.length; i++) {
        total += order.items[i].price;
    }

    if (order.user.role === "VIP") {
        total *= 0.8;
    }

    console.log("Order total:", total);
    console.log("Order placed by:", order.user.name);

}

Problem:
-This function calculates totals, applies discounts, and prints information.

Refactored version:
function calculateTotal(items) {
let total = 0;
for (let i = 0; i < items.length; i++) {
total += items[i].price;
}
return total;
}

function applyDiscount(total, user) {
if (user.role === "VIP") {
return total \* 0.8;
}
return total;
}

function printOrderSummary(total, user) {
console.log("Order total:", total);
console.log("Order placed by:", user.name);
}

function processOrder(order) {
let total = calculateTotal(order.items);
total = applyDiscount(total, order.user);
printOrderSummary(total, order.user);
}

Each function now has one responsibility.

_Duplicate Code_

Example:
function printUser(user) {
console.log("Name:", user.name);
console.log("Email:", user.email);
}

function printAdmin(admin) {
console.log("Name:", admin.name);
console.log("Email:", admin.email);
}

Problem:
-The printing logic is duplicated.

Refactored version:
function printPerson(person) {
console.log("Name:", person.name);
console.log("Email:", person.email);
}

Now the logic exists in one place.

_Large Class (God Object)_

Example:
class UserManager {
createUser() {}
deleteUser() {}
sendEmail() {}
generateReport() {}
calculateStatistics() {}
}

Problem:
-This class handles too many responsibilities.

Refactored version:
class UserService {
createUser() {}
deleteUser() {}
}

class EmailService {
sendEmail() {}
}

class ReportService {
generateReport() {}
calculateStatistics() {}
}

Responsibilities are separated.

_Deeply Nested Conditionals_

Example:
function checkAccess(user) {
if (user) {
if (user.isActive) {
if (user.role === "admin") {
console.log("Access granted");
}
}
}
}

Problem:
Hard to read due to deep nesting.

Refactored version:
function checkAccess(user) {
if (!user) return;
if (!user.isActive) return;
if (user.role !== "admin") return;

    console.log("Access granted");

}

Now it is cleaner and easier to follow.

_Commented-Out Code_

Example:
function calculateTotal(price) {
// let discount = price \* 0.1;
// return price - discount;
return price;
}

Problem:
-Unused code should be removed instead of commented out.

Refactored version:
function calculateTotal(price) {
return price;
}

Version control systems like Git already track old code.

_Inconsistent Naming_
Example with code smell
let usrNm = "John";
let totalAmount = 100;
let x = true;

Problem:
Names are inconsistent and unclear.

Refactored version:
let userName = "John";
let totalOrderAmount = 100;
let isActive = true;

Names are now clear and consistent.

**Reflection**

1. What code smells did you find in your code?

In my code, I found several code smells including magic numbers, long functions, duplicate logic, deeply nested conditionals, inconsistent naming, and commented-out code. Some functions were doing too many things at once, and some values were hardcoded without explanation. There were also areas where logic was repeated instead of reused.

## How did refactoring improve the readability and maintainability of the code?

Refactoring improved the structure of the code by separating responsibilities into smaller functions and classes. It removed duplication and replaced magic numbers with clearly named constants. Deep nesting was reduced by using guard clauses, which made the logic easier to follow. Variable names were improved to better describe their purpose. Overall, the code became cleaner, shorter, and easier to understand.

2. How can avoiding code smells make future debugging easier?

Avoiding code smells makes debugging easier because the code becomes more organized and predictable. When logic is not duplicated, fixing a bug in one place automatically fixes it everywhere. Smaller functions are easier to test and inspect. Clear names and simple structures reduce confusion when reading the code. This helps developers find problems faster and make changes with more confidence.
