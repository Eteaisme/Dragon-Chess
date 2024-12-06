### Adapted From 8033's FRC Training Docs

## Git is a version control system, or a way for us to collaborate on code and manage having multiple versions of code working in parallel

While many modern cloud applications, like google docs, have some form of auto-save to the cloud, we don't necessarily want a single auto-updating version of our code.
Instead we use a tool called Git to manage different versions of our files and save them to Github, which lets us share the codebase between computers.
Instead of automatically syncing to Github, we save our code in small named chunks called commits.
The named versions makes it easy to revert changes that break previously working behavior and see when and by who code was written.
Git also lets us have different versions, called branches, in progress in parallel.
This means that while one person works on code for the autonomous, another could work on vision, for example.

### Resources

- [WPILib Git intro](https://docs.wpilib.org/en/stable/docs/software/basic-programming/git-getting-started.html)
- [Github Git intro](https://docs.github.com/en/get-started/using-git/about-git)
- _Record quick intro to git vid/talk at some point, talk to kevin or a software lead until then_
- [Git install](https://gitforwindows.org/)

### Examples

- ![A simple demonstration of commiting and pushing some changes in git](../../Assets/GitExample.png)
- Typing `git add .` then `git commit -m "commit name"` then `git push` is the bread and butter of using git.
  This sequence takes all of your uncommited changes and commits them, then pushes them to github
- `git checkout branch-name` switches between branches
- `git checkout -b new-branch` makes a new branch and switches to it.
  Note that the first time you push from this branch you will need to enter some extra parameters, but the terminal should prompt you with the correct command when you enter `git push`
- `git status` displays the current branch and what changes you have uncommited and staged
- `git pull` updates the code on your device with the latest code from Github.
  Recommended to do this whenever someone else has been working on the same branch, otherwise you might make conflicting changes
- [A simple demo video of commiting some changes](../../Assets/GitDemoVideo.mp4)
