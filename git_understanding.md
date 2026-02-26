The conflict happened because the same line in the file was modified in two different branches. When merging, Git could not decide which version to keep. And so, in Github Desktop, I resolved the conflict by choosing one version of the file (use the modified file from main) and then completes the merge.

I learned that Git conflicts happen when the same file is changed in different branches. To fix them, you need to decide how the changes should be combined so nothing important is lost. This showed me why communication and coordination when working in a team is very important to avoid conflicts.

1. What makes a good commit message?

A good commit message is clear, short, and specific. It explains what was changed and sometimes why it was changed. It should be easy to understand without being too long. A well-written commit message helps anyone quickly understand the purpose of the change.

2. How does a clear commit message help in team collaboration?

Clear commit messages help team members understand changes without reading all the code. When working in a team, developers rely on commit history to track progress and fix issues. Good commit messages make collaboration smoother and reduce confusion.

3. How can poor commit messages cause issues later?

Poor commit messages like “fix” or “update” do not explain what was changed. This can cause problems later when someone tries to debug or review old changes. Without clear messages, it becomes harder to understand the history of the project, which can slow down development.