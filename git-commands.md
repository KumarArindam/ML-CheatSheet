### search (regex)
```
git grep "regex"
```

### list all branches
```
git branch -a
```

### list remote branches
```
git branch -r
```

### checkout an branch on remote
make sure you don't use `origin`
```
git fetch
git checkout branchName
```

### Create a new branch
first create a branch
```
git checkout -b <branchName>
```

Create a new branch from an existing branch
```
git checkout origin/branchName -b newBranchName
```

Then push your new branch to the repo
```
git push origin <branchName>
```

### Create a branch from a commit
AKA Recover a deleted branch
```
git checkout -b <branch> <sha>
```

### revert all changes in a branch. Removes staged and working directory changes.
```
git reset --hard
```

### Resets index to former commit; replace `56e05fced` with your commit code. You can use git log to get commit code
```
git reset 56e05fced
```

### revert a file to the most recent commit
```
git checkout HEAD -- /somePath/file.txt
```

### undo the last commit. Blow it out of the water.
```
git reset --hard HEAD~1
```

### undo your last commit but leave the files from that commit staged. 
```
git reset --soft HEAD~1
```

### delete local (untracked) files
```
git clean -f
```

### If you want to also remove directories, run 
```
git clean -f -d
```

### to discard changes in working directory
```
git checkout -- <file>
```

### Checkout a file from another branch
```
git checkout origin/branchName  -- fileName.txt
```

### clean a folder
```
git clean -fxd {dir_path}
```

### commit a folder/file without staging it.
```
git commit /folderToCommit -m 'commit msg'
```

### list all branches (remote & local/remote only)
```
git branch -a
git branch -r
```

### Find out all branches a commit is on
```
git branch --contains <commit>
```

### display log with Tree
```
git log --pretty=format:"%h - %cr (%an) %s" --graph
```

### Merge Master into your local branch
```
git fetch
git merge origin/master
```
a shortcut to this is. They are both the same 
```
git pull origin master
```
or, if it's a busy repo.
```
git pull --rebase <remote name> <branch name>
```

### list conflicts
```
git diff --name-only --diff-filter=U
grep -lr '<<<<<<<' .
```

### Diff a conflict
```
git mergetool -t opendiff
```

### pull a branch , merge if conflicted use remote.
```
git pull -s recursive -X theirs origin ra
```

### show log with merged files
```
git log -m -1 --name-only
```

### Show the changes between two branches.
```
git diff --name-status master..branchName > changelog.txt
```

### Recover a deleted branch

Get the SHA of the last commit on the branch.

```
git checkout -b newbranchname 56e05fced
```

## Stashes

### save a stash
```
git stash save "My changes."
```

### list your saved stashes
```
git stash list
```

### apply a stash (Where stash@{1} is the stash you want to apply.)
```
git stash apply stash@{1}
```

### delete a branch on origin
```
git push origin --delete <branchName>
```

### delete a branch locally
```
git branch -d <branchName>
```

### remove local branches that are not on remote
```
git remote prune origin
```

### Get all commits from a branch. For a release log, changelog etc.
```
git cherry -v develop mybranch
```

### Revert a commit that is onrigin/remote

This reverts the commit with a new commit.

First get the commit sha.

```
git revert -m 1 <commit-hash> 
git commit -m "Reverting the last commit which messed the repo."
git push -u origin master
```

# Utilities

### Get the status on all repos in a folder
```
find . -maxdepth 1 -mindepth 1 -type d -exec sh -c '(echo {} && cd {} && git status -s && echo)' \;
```

Save the results to a file.
```
find . -maxdepth 1 -mindepth 1 -type d -exec sh -c '(echo {} && cd {} && git status -s && echo)' \; > gitreport.txt
```

### Delete all local branches that don't exist on `origin`

run `git fetch -p` this removes the remote references.

run `git branch -vv`

then run the following script

```
git fetch -p && for branch in `git branch -vv | grep ': gone]' | awk '{print $1}'`; do git branch -D $branch; done
```