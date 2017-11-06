
# Git Workflow:
## create and checkout from master
`git pull --rebase`

`git checkout -b branch-name`

## patching changes before commit
`git add -p` # patch

**y/n** commit yes or no?

## git commit selected patched changes (from above)
`git commit -m "COMMIT MESSAGE"`

## rebase master branch before squashing, pushing & merging
`git checkout master`  # go to master branch

`git pull --rebase`  # updates master branch

`git checkout branch-name`  # go back to new branch

`git rebase -i master`  # to get clean history squashing etc.
  exit = **ctrl+x** and yes=**y**

`git push -f origin branch-name:branch-name`  # force (-f) push changes

## Go to git.com pull request and merge branch into master

## Pull merged master branch
`git pull --rebase`
`git -D branch-name`  # delete branch-name if not needed anymore


#Save password:
`git config --global user.email juko@dhigroup.com`

`git config credential.helper store`

`git pull` # from repo credentials are stored in conda
