The conflict happened because the same line in the file was modified in two different branches. When merging, Git could not decide which version to keep. And so, in Github Desktop, I resolved the conflict by choosing one version of the file (use the modified file from main) and then completes the merge.

I learned that Git conflicts happen when the same file is changed in different branches. To fix them, you need to decide how the changes should be combined so nothing important is lost. This showed me why communication and coordination when working in a team is very important to avoid conflicts.

===================================================================================================

1. What makes a good commit message?

A good commit message is clear, short, and specific. It explains what was changed and sometimes why. It should be easy to understand without reading the entire code. A well-written commit message helps anyone quickly understand the purpose of the change.

2. How does a clear commit message help in team collaboration?

Clear commit messages help team members understand changes without having to read all the code. In a team project, developers rely on commit history to track progress, debug, or review features. Good commit messages make collaboration smoother and reduce confusion.

3. How can poor commit messages cause issues later?

Poor commit messages like “fix” or “update” do not explain what was changed. This can cause problems later when debugging or reviewing old commits. Without clear messages, it becomes harder to understand the history of the project, slowing down development and increasing the chance of errors.

Proof of hands-on commits in commits.txt:

PS C:\intern\myl-intern-repo> git log --oneline -- commits.txt
a5d6b31 Improve test case formatting
7f478f9 fixed the issue where the test file was not properly structured because I forgot to include the correct formatting and indentation and this might affect future test cases if not corrected immdiately
65bbd70 fixed stuff

Description of each commit:
-The first commit, fixed stuff, is vague. It provides almost no information about what was changed. While it technically records a change, it does not help anyone reading the commit history understand the purpose of the update.

-The second commit, fixed the issue where the test file was not properly structured because I forgot to include the correct formatting and indentation and this might affect future test cases if not corrected immdiately, is overly detailed. Although it clearly explains what was done, the message is too long for a commit log. It reads more like a paragraph and is difficult to scan quickly, which reduces clarity.

-The third commit, Improve test case formatting, is well-structured. It is concise, clear, and communicates exactly what was changed in a single line. This makes it easy to read in the commit history while providing enough context for someone reviewing the code later.

File contents in commits.txt:
vague commit
overly detailed commit
well-structured commit

==================================================================================================

1. What does git bisect do?

git bisect helps find the exact commit that introduced a bug in your code by using a binary search approach.
You tell Git a “good” commit (working code) and a “bad” commit (broken code), and Git automatically checks commits in between. By marking each as good or bad while testing, Git quickly narrows down the commit that caused the issue.

Example from my hands-on:
-Good commit → Version 1 (console.log("Version 1 - working"))
-Bad commit → Version 4 (Version 4 - additional change)
-Git automatically checked Version 2 and Version 3. After testing, it identified Version 3 (consol.log) as the first bad commit.

2. When would you use it in a real-world debugging situation?

You would use git bisect when a feature was previously working but suddenly breaks, and you don’t know which commit introduced the bug.

Example scenario:

-In a large project with many commits from multiple developers, a function stops working.
-Instead of manually checking dozens of commits, git bisect lets you test only a few selected commits to quickly isolate the problem.
-In my experiment, I used it to pinpoint the intentional typo in Version 3.

3. How does it compare to manually reviewing commits?

-Faster: Git bisect reduces the number of commits to test by half each time (binary search).
-More reliable: Manually reviewing code can miss subtle bugs or mistakes.
-Hands-on proof: Running node app.js during bisect confirmed exactly which commit caused the error.

Contrast with manual review:

-If I had checked each of the 4 commits one by one manually, it would take longer.
-Git bisect immediately told me that Version 3 was the first bad commit, saving time and reducing human error.

Terminal Commands/Output from the hands-on:

PS C:\Users\johnm> cd C:\intern\myl-intern-repo
PS C:\intern\myl-intern-repo> git add app.js
PS C:\intern\myl-intern-repo> git commit -m "Version 1 - working" --no-verify
[main ba4ad08] Version 1 - working
1 file changed, 1 insertion(+), 1 deletion(-)
PS C:\intern\myl-intern-repo> git add app.js
PS C:\intern\myl-intern-repo> git commit -m "Version 2 - still working" --no-verify
[main dfd05d8] Version 2 - still working
1 file changed, 1 insertion(+)
PS C:\intern\myl-intern-repo> git add app.js
PS C:\intern\myl-intern-repo> git commit -m "Version 3 - broken (intentional bug)" --no-verify
[main 6bce3cb] Version 3 - broken (intentional bug)
1 file changed, 1 insertion(+)
PS C:\intern\myl-intern-repo> git add app.js
PS C:\intern\myl-intern-repo> git commit -m "Version 4 - additional change" --no-verify
[main e639303] Version 4 - additional change
1 file changed, 1 insertion(+)
PS C:\intern\myl-intern-repo> git log --oneline
e639303 (HEAD -> main) Version 4 - additional change
6bce3cb Version 3 - broken (intentional bug)
dfd05d8 Version 2 - still working
ba4ad08 Version 1 - working
PS C:\intern\myl-intern-repo> git bisect start
status: waiting for both good and bad commits
PS C:\intern\myl-intern-repo> git bisect bad
status: waiting for good commit(s), bad commit known
PS C:\intern\myl-intern-repo> git bisect good HEAD~3
Bisecting: 0 revisions left to test after this (roughly 1 step)
[6bce3cb05f3420b69485941ab2690bee5297d6ce] Version 3 - broken (intentional bug)
PS C:\intern\myl-intern-repo> node app.js
Version 1 - working
Version 2 - still working
C:\intern\myl-intern-repo\app.js:3
consol.log('Version 3 - broken'); // intentional typo
^

ReferenceError: consol is not defined
at Object.<anonymous> (C:\intern\myl-intern-repo\app.js:3:1)
at Module.\_compile (node:internal/modules/cjs/loader:1688:14)
at Object..js (node:internal/modules/cjs/loader:1820:10)
at Module.load (node:internal/modules/cjs/loader:1423:32)
at Function.\_load (node:internal/modules/cjs/loader:1246:12)
at TracingChannel.traceSync (node:diagnostics_channel:322:14)
at wrapModuleLoad (node:internal/modules/cjs/loader:235:24)
at Function.executeUserEntryPoint [as runMain] (node:internal/modules/run_main:171:5)
at node:internal/main/run_main_module:36:49

Node.js v22.18.0
PS C:\intern\myl-intern-repo> git bisect bad
Bisecting: 0 revisions left to test after this (roughly 0 steps)
[dfd05d86019019fcd4900f0458886a2986ed5d91] Version 2 - still working
PS C:\intern\myl-intern-repo> node app.js
Version 1 - working
Version 2 - still working
PS C:\intern\myl-intern-repo> git bisect good
6bce3cb05f3420b69485941ab2690bee5297d6ce is the first bad commit
commit 6bce3cb05f3420b69485941ab2690bee5297d6ce
Author: pekaboo01 <167494554+pekaboo01@users.noreply.github.com>
Date: Tue Mar 17 10:24:26 2026 +0800

    Version 3 - broken (intentional bug)

app.js | 1 +
1 file changed, 1 insertion(+)

=========================================================================================================

1. Difference Between Staging and Committing?

- Staging is the process of preparing changes to be committed. Changes are added to the staging area but are not yet part of the repository history.
- Committing is the process of saving staged changes into the repository history as a snapshot.

2. Why Git Separates These Two Steps?

- Separation allows more control over which changes go into a commit.
- Helps in organizing commits logically instead of committing everything at once.
- Enables selective committing when working on multiple features or fixes simultaneously.

3. When to Stage Changes Without Committing

- When working on multiple tasks in the same file but want to commit each task separately.
- When reviewing changes before making a permanent record.
- When preparing commits with partial changes (only some lines of a file).

=========================================================================================================

1. Why is pushing directly to main problematic?

Pushing directly to the main branch can be risky because it may introduce untested or incomplete changes to the codebase. In a team setting, this can break the project for everyone else, make it harder to track who made which changes, and reduce the overall stability of the repository.

2. How do branches help with reviewing code?

Branches allow developers to work on features, bug fixes, or experiments in isolation from the main branch. This separation makes it easier to review code before merging it, ensures that the main branch remains stable, and allows for structured collaboration, such as using pull requests or code reviews to check changes.

3. What happens if two people edit the same file on different branches?

If two people modify the same file on different branches, Git will keep their changes separate until the branches are merged. During the merge, if the changes conflict, Git will prompt for a manual resolution. This ensures that both contributions are considered and integrated carefully without automatically overwriting anyone’s work.

============================================================================================================

1. What does each command do and when would you use it?

_git checkout main -- <file>_ restores a specific file from the main branch without affecting other changes in your working branch. This is useful when you accidentally modify a file but want to revert it to the version in main without discarding other work.
_git cherry-pick <commit>_ applies a specific commit from another branch onto your current branch. This is valuable when you need a particular change from another branch without merging all the changes, allowing selective updates to maintain stability.
**git log\* displays the commit history of a branch, showing messages, authors, and timestamps. It is essential for understanding how a project has evolved, tracking down changes, and reviewing the sequence of commits.
**git blame <file>\* shows line-by-line information about who last modified each line and when. This helps identify the author of a specific change, debug issues, or understand why a particular modification was made.

2. What surprised you while testing these commands?

Testing these commands highlighted how precise Git can be. I was surprised by how git cherry-pick allows selective application of changes without affecting the rest of a branch, which is incredibly powerful in long-running projects. Using git checkout main -- <file> also showed me how easy it is to undo mistakes without losing other work. git blame was enlightening because it quickly revealed the history of each line in a file, making collaboration and debugging much easier.

=================================================================================================================

1. What is a Pull Request (PR), and why is it used?

A Pull Request (PR) is a feature in GitHub that allows a developer to propose changes made in a branch and request that those changes be reviewed before merging them into the main branch. It is used to compare differences between branches, discuss modifications, request improvements, and ensure code quality before integration.

PRs are important because they create a structured review process. Instead of directly pushing changes to the main branch, team members can review the code, suggest improvements, and confirm that it meets project standards. This reduces errors, improves collaboration, and maintains stability in the repository.

_Reflection_

1. Why are PRs important in a team workflow?

PRs are important because they ensure that code is reviewed before being merged. This helps catch bugs early, maintain coding standards, and improve overall quality. PRs also encourage collaboration since team members can discuss improvements before finalizing changes.

2. What makes a well-structured PR?

-A well-structured PR includes:
-A clear and descriptive title
-A detailed explanation of what was changed
-The reason for the change
-Screenshots or logs if needed
-A link to the related issue
-Clean and focused commits (no unrelated changes)

A good PR makes it easy for reviewers to understand the purpose and impact of the changes.

3. What did you learn from reviewing an open-source PR?

From reviewing an open-source PR, I learned that clear communication is just as important as writing good code. Reviewers often focus on readability, structure, and long-term maintainability. I also noticed that feedback is specific and constructive, which helps improve the final output.

This experience showed me that PRs are not just about merging code, but about improving quality through collaboration and discussion.
