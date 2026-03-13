1. What are the most common reasons for E2E test failures?

E2E tests often fail because of timing issues (like elements loading slowly), dynamic UI changes, missing elements, or unexpected pop-ups/errors in the app.

2. How do you determine if a test is flaky?

A test is flaky if it sometimes passes and sometimes fails without any changes to the code. You can check by running it multiple times and seeing inconsistent results.

3. What strategies can you use to improve test reliability?

-Using explicit waits for elements to appear
-Retrying actions if they fail
-Making tests independent of each other
-Handling dynamic UI elements carefully

4. How can logging and screenshots help with debugging test failures?

Logging shows exactly what steps ran and what errors happened. Screenshots show what the app looked like at the time of failure. Together, they help you quickly find and fix problems.
