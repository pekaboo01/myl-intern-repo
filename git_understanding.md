The conflict happened because the same line in the file was modified in two different branches. When merging, Git could not decide which version to keep. And so, in Github Desktop, I resolved the conflict by choosing one version of the file (use the modified file from main) and then completes the merge.

I learned that Git conflicts happen when the same file is changed in different branches. To fix them, you need to decide how the changes should be combined so nothing important is lost. This showed me why communication and coordination when working in a team is very important to avoid conflicts.

===================================================================================================

1. What makes a good commit message?

A good commit message is clear, short, and specific. It explains what was changed and sometimes why it was changed. It should be easy to understand without being too long. A well-written commit message helps anyone quickly understand the purpose of the change.

2. How does a clear commit message help in team collaboration?

Clear commit messages help team members understand changes without reading all the code. When working in a team, developers rely on commit history to track progress and fix issues. Good commit messages make collaboration smoother and reduce confusion.

3. How can poor commit messages cause issues later?

Poor commit messages like “fix” or “update” do not explain what was changed. This can cause problems later when someone tries to debug or review old changes. Without clear messages, it becomes harder to understand the history of the project, which can slow down development.

==================================================================================================

1. What does git bisect do?

Git bisect helps you find the specific commit that introduced a bug in your code by using a binary search approach. You mark a known “good” commit and a known “bad” commit, and Git automatically checks out the commits in between so you can test them. By repeatedly marking commits as good or bad, Git quickly narrows down which commit caused the issue, saving you from manually checking every single commit.

2. When would you use it in a real-world debugging situation?

You would use git bisect when you know your code was working at some point, but now a bug exists, and you don’t know which commit introduced it. For example, if a feature suddenly breaks after several days of commits, bisect allows you to pinpoint the exact commit responsible without reviewing every change manually. This is especially helpful in projects with many commits or multiple developers.

3. How does it compare to manually reviewing commits?

Git bisect is much faster and more efficient than manually reviewing commits. Instead of looking at every single change, bisect uses a binary search, meaning it tests roughly half of the commits each time. Manual review can be very slow and prone to human error, especially in large projects, whereas bisect quickly isolates the problem commit while letting you focus only on testing the code behavior.

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