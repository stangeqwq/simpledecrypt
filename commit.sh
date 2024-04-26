#!/bin/bash

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
