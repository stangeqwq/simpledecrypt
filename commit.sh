#!/bin/bash
# for some reason crontab can't get permission to run this (VERY ANNOYING UGHHH)
# convert to python instead that works (checked using simple everyminute cron print "hello")

# Specify the path to your Git repository
GIT_REPO_PATH="/Users/stange/Desktop/misc/simpledecrypt"

# Specify the name of the text file to modify (relative to the repository root)
TEXT_FILE="filename.txt"

# Navigate to the Git repository directory
cd "$GIT_REPO_PATH" || exit

# Add "commit" to the text file
echo "commit" >> "$TEXT_FILE"

# Stage the changes
git add "$TEXT_FILE"

# Commit the changes with a message
git commit -m "Automatically add 'commit' to $TEXT_FILE"

# Push the comit
git push

# have the script running in a cronttab every hour, every day, for green :D
