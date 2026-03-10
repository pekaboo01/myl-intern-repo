1. How does running tests in CI/CD help maintain application stability?

Running tests in CI/CD ensures that every change in the code is automatically checked. If something breaks, the test fails and stops deployment. This keeps the application stable because broken features never reach users.

2. What are the challenges of running GUI-based tests (Pywinauto) in CI/CD pipelines?

-They need a desktop interface, not just a command line.
-Windows apps may load slowly or behave differently (like Notepad in Windows 11).
-Tests can be flaky if UI elements change or are not ready in time.

3. How can flaky tests be handled in a CI/CD environment?

Flaky tests can be handled by improving test stability and adding retries. Tests should wait for UI elements properly instead of relying on fixed delays. Logging and screenshots can also help identify the cause of failures. If a test fails randomly, retrying the test can prevent unnecessary pipeline failures.

4. What would be the next steps to fully integrate Focus Bear’s automated tests into its deployment pipeline?

The next steps would include creating a CI workflow that runs automated tests on a Windows environment, installing all required dependencies, and running the Pywinauto tests automatically after each code push. Test results should be reported in the CI system, and deployment should only proceed if all tests pass.
