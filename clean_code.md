Clean Code Principles

1. *Simplicity* means writing code that is straightforward and avoids unnecessary complexity. The simpler the code, the easier it is to understand, test, and debug. Complex solutions may seem impressive, but they often create confusion and increase the risk of errors.

Simple code focuses on solving the problem directly without adding extra features or logic that are not needed. It follows the idea of doing one thing well instead of trying to handle everything at once.

2. *Readability* means that the code should be easy for other developers to understand. This includes using clear variable names, proper formatting, consistent indentation, and meaningful comments when necessary.

Code is read more often than it is written. If someone cannot quickly understand what the code is doing, it becomes harder to maintain and improve. Good readability reduces misunderstandings and mistakes.

3. *Maintainability* means that the code should be easy to modify or extend in the future. Software projects evolve over time, and changes are inevitable. If the code is messy or tightly coupled, making updates becomes difficult and risky.

Maintainable code is modular, well-structured, and organized into small reusable functions. This makes it easier for future developers — including yourself — to improve the code without breaking existing functionality.

4. *Consistency* means following the same coding style, naming conventions, and structure throughout the project. This includes consistent formatting, file organization, and function naming.

When code is consistent, it feels predictable and easier to navigate. Teams often follow style guides to ensure everyone writes code in a similar way. This improves collaboration and reduces confusion.

5. *Efficiency* means writing code that performs well and uses resources wisely. However, it is important to avoid premature optimization. Code should first be correct and readable before being optimized.

Efficient code improves performance, but it should not sacrifice clarity. A balance between performance and simplicity is important in real-world development.

**Messy code example:**

function x(a,b){if(a>0){if(b>0){return a*b}else{return 0}}else{return 0}}

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

  return numberOne * numberTwo;
}

This is cleaner simply because:

-The function name clearly describes its purpose.
-Variable names are meaningful.
-Proper formatting improves readability.
-The condition is simplified.
-The logic is easier to follow.

And so, clean code principles are important because they improve collaboration, reduce bugs, and make future updates easier. Writing simple, readable, maintainable, consistent, and efficient code ensures that projects remain stable and scalable over time.