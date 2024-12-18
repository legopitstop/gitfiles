import gitfiles

# Load all .gitignore files
gitfiles.load_gitignore()

# Returns True because .gitingore contains `*.so`
print(gitfiles.match("test.so"))
