git help <Command name> WILL HELP YOU A LOT. 🙃🙃
===================================================
Convert a directory in to git repository
* `git init`

### Add your email and user id
- `git config --global user.name '<choose a user name>'`
- `git config --global user.email '<enter a email id>'`

### Check current status of your repository
- `git status`
- `git status -s`

### Check changes made
- `git log`
- `git log -p -<any number>`

### addition if files to staging area
- `git add .`
- `git add -A`
- `git add .`
- `git add <file name>`

### COMMIT COMMANDS. 
- `git commit`
- `git commit -m "<your reason>"`
- `git commit -a -m "<your reason>"`

### COMMAND TO REMOVE FILES FROM GOT REPORITRY. 
- `git rm <file name> `
- `UNSTAGE YOUR FILES`
- `git rm --cached <file name>`

### BRANCH RELATED
- `git branch` command to change number and name of branches

- `git branch <name of new branch>` creating a new branch
- `git checkout -b <branch name>` creats a new branch and automatically switch to it.
- `git branch -d <name of branch>`
And
`git branch --delete <name of branch>`
[Will delete a branch at local level. ]


@ TO CHANGE BRANCHES. 
- `git checkout <branch name>`
- `git checkout <file name>`
- `git switch <name of a existing branch>`


@ MATCH FILES TO THE LAST COMMIT. 
- `git checkout -f `
- `git restore <filename>`

@ MERGE 2 BARNCHES
- `git merge <branch name>`

@ PUSHING AND PULLING FILES. 
- `git push -u origin <name of repository>`
- `git push `
git pull
- `git fetch `[will pull all branches from remote repository]
`git diff` <compare file in working tree with staging area>
- `git diff --stagged <compare the file in staging area with last committed file>`







@ COMMAND TO PUSH A NEW BRANCH $
- `git push --set-upstream origin <branch name>`





@ RENAMING A GIT BRANCH $

- `git checkout <old_name>`
  [Will change your current branch ti "old_name"]

- `git branch -m <new_name>`
  [Will rename your branch locally]

- `git push origin -u <new_name>`
  [Will push renamed branch to remote reporitry]

- `git push origin --delete <old_name>`
  [Eill delete "old_name" from remote reporitry]


===================================================
@ COMMANDS STILL TO UNDERSTAND $
```
restore
Mv 
Rm
Sparse-checkout
Reset
Tag
```
===================================================


FOR MORE RUN "git help git" COMMAND ON YOUR TERMINAL

===================================================

TERMINOLOGY

⚠️ there might be some exceptions. 

Thanks
