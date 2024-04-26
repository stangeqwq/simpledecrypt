import subprocess
import os

# Specify the path to your Git repository
GIT_REPO_PATH = "/Users/stange/Desktop/misc/simpledecrypt"

# Specify the name of the text file to modify (relative to the repository root)
TEXT_FILE = "filename.txt"

# Navigate to the Git repository directory
os.chdir(GIT_REPO_PATH)

# Add "commit" to the text file
with open(TEXT_FILE, 'a') as file:
    file.write("commit\n")

# Stage the changes
subprocess.run(["git", "add", TEXT_FILE])

# Commit the changes with a message
commit_message = f"Automatically add 'commit' to {TEXT_FILE}"
subprocess.run(["git", "commit", "-m", commit_message])

# Push the changes
subprocess.run(["git", "push"])


# have the script running in a cronttab every hour, every day, for green :D