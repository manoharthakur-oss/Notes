git help <Command name> WILL HELP YOU A LOT. 🙃🙃
===================================================

* `git init`

- `git config --global user.name '<choose a user name>'`
- `git config --global user.email '<enter a email id>'`

- `git status`
- `git status -s`

- `git log`
- `git log -p -<any number>`

- `git add .`
- `git add -A`
- `git add <file name>`

@ COMMIT COMMANDS. 
- `git commit`
- `git commit -m "<your reason>"`
- `git commit -a -m "<your reason>"`

@ COMMAND TO REMOVE FILES FROM GOT REPORITRY. 
- `git rm <file name> `
- `UNSTAGE YOUR FILES`
- `git rm --cached <file name>`

@ BRANCH RELATED
- `git branch`

- `git branch <name of new branch>`

- `git branch -d <name of branch>`
And
`git branch --delete <name of branch>`
[Will delete a branch at local level. ]


@ TO CHANGE BRANCHES. 
git checkout <branch name>
git checkout -b <branch name>
git checkout <file name>
git switch <name of a existing branch>


@ MATCH FILES TO THE LAST COMMIT. 
git checkout -f 

git restore <filename>

@ MERGE 2 BARNCHES
git merge <branch name>

@ PUSHING AND PULLING FILES. 
git push -u origin <name of repository>
git push 
git pull
git fetch [will pull all branches from remote repository]
git diff <compare file in working tree with staging area>
git diff --stagged <compare the file in staging area with last committed file>
git fetch [pulls all branches from remote reporitry]






@ COMMAND TO PUSH A NEW BRANCH $
git push --set-upstream origin <branch name>





@ RENAMING A GIT BRANCH $

git checkout <old_name>
  [Will change your current branch ti "old_name"]

git branch -m <new_name>
  [Will rename your branch locally]

git push origin -u <new_name>
  [Will push renamed branch to remote reporitry]

git push origin --delete <old_name>
  [Eill delete "old_name" from remote reporitry]


===================================================
@ COMMANDS STILL TO UNDERSTAND $

restore
Mv 
Rm
Sparse-checkout
Reset
Tag

===================================================


FOR MORE RUN "git help git" COMMAND ON YOUR TERMINAL

===================================================

TERMINOLOGY

⚠️ there might be some exceptions. 

Thanks
