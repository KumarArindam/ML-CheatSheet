# Hackfest18
#### Guide for contributors:
1. Fork this repository
2. Click on clone or download and then 'copy to clipboard'
3. Open git bash in a folder
4. Type `git clone` and hit `Shift + Ins`
5. After modifying files, git bash into '.../Hackfest18'
- `git diff` to show file differences not yet staged
- `git add [file]` to stage the file before committing
- `git diff --staged` to show file differences between staging and the last file version
- `git reset [file]` to unstage the file, but preserve its contents
- `git commit -m "[descriptive message about the commit]"` to permanently commit the file into version history
6. For experimental changes, it is advisable to open a new branch of the repository as follows
- `git branch` lists all local branches in the current repository
- `git branch [branch-name]` creates a new branch
- `git checkout [branch-name]` switches to the specified branch and updates the working directory
- `git merge [branch]` combines the specified branch's history into the current branch
- `git branch -d [branch-name]` deletes the specified branch

7. To update your fork on GitHub with the recent changes, do the following
- Go to your fork on GitHub
- Click on clone or download and then 'copy to clipboard'
- Open git bash in the local repository folder and type the following
- `git remote` lists all the aliases.
- If you do not see an alias called origin, follow the next step
- `git remote add origin` and hit `Shift + Ins` (one-time process)
- `git push origin [branch-name]` pushes the branch to the remote repository
- `git push origin master` pushes your latest changes into the master branch of your fork

8. To update the changes to the original repository, do the following
- Go to your fork
- If you see the message 'Able to merge', go ahead and click on 'Pull request'
- Otherwise, resolve the discrepancies and try again

9. To update your local clone with the latest changes, do the following
- Go to the original repository [here](https://github.com/sv-cheats1/Hackfest18)
- Click on clone or download and then 'copy to clipboard'
- Open git bash in the local repository folder and type the following
- `git remote add upstream` and hit `Shift + Ins`
- `git fetch upstream` fetches all the branches of that remote into remote-tracking branches
- `git checkout master` makes sure that you're on your master branch
- `git rebase upstream/master` rewrites your master branch so that any commits of yours that aren't already in upstream/master are replayed on top of that other branch

10. To update your fork on GitHub, follow step 7
- `git push origin master` will do the trick most of the time